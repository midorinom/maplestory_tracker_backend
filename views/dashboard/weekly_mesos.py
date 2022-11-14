from app import db
from flask import request, jsonify, Blueprint
from models.dashboard.WeeklyMesos import WeeklyMesos, weekly_mesos_schema
import datetime
from models.dailies.UrsusTour import UrsusTour, ursus_tour_schema
from models.farming.Farming import Farming, farming_schema
from models.dashboard.Characters import Characters
from functools import reduce


weekly_mesos_blueprint = Blueprint("weekly_mesos", __name__)


# Get Weekly Mesos
@weekly_mesos_blueprint.post("/weekly-mesos/get")
def get_weekly_mesos():
    json_data = request.get_json()

    try:
        # Using today's date, get the first_day_of_bossing_week
        date_list = json_data["date"].split("-")
        date_list = [int(i) for i in date_list]
        date = datetime.date(*date_list)

        # timedelta subtracts the current weekday (converted to a value) from today's date, to get Monday's date
        # Then add 3 to get Thursday, which is the day when the bossing week resets
        # The operation involving timedelta returns a datetime Object. strftime formats it back to a string
        first_day_of_bossing_week = (date + datetime.timedelta(days=-date.weekday()+3)).strftime("%Y-%m-%d")

        # Remove date from json_data, add first_day_of_bossing_week, then load json_data
        json_data.pop("date")
        json_data["first_day_of_bossing_week"] = first_day_of_bossing_week

        data = weekly_mesos_schema.load(json_data)

        # Check if there is an existing entry for this week. If there is none, make a new entry for this week
        weekly_mesos = weekly_mesos_schema.dump(
            WeeklyMesos.query.filter(
                WeeklyMesos.username == data["username"],
                WeeklyMesos.first_day_of_bossing_week == first_day_of_bossing_week), many=True)

        if len(weekly_mesos) == 0:
            # Make a new entry for this week
            first_day_of_bossing_week = date + datetime.timedelta(days=-date.weekday()+3)
            new_weekly_mesos = WeeklyMesos(
                username=data["username"], first_day_of_bossing_week=first_day_of_bossing_week)

            db.session.add(new_weekly_mesos)
            db.session.commit()

        # Query for the ursus_tour entries for this week
        ursus_tour = ursus_tour_schema.dump(
            UrsusTour.query.filter(
                UrsusTour.username == data["username"],
                UrsusTour.first_day_of_bossing_week == first_day_of_bossing_week), many=True)

        # If there are entries, sum up the total mesos for ursus and tour respectively
        if len(ursus_tour) > 0:
            ursus = [element["ursus"] for element in ursus_tour]
            tour = [element["tour"] for element in ursus_tour]

            ursus_total = reduce(lambda a, b: a + b, ursus)
            tour_total = reduce(lambda a, b: a + b, tour)
        else:
            ursus_total = 0
            tour_total = 0

        # Query for the farming entries for this week
        # Raw: SELECT * from farming WHERE character IN(SELECT uuid from characters WHERE username = data["username"])
        farming = farming_schema.dump(
            Farming.query.filter(
                Farming.character.in_(
                    Characters.query.filter(
                        Characters.username == data["username"]).with_entities(Characters.uuid))), many=True)

        # If there are entries, sum up total mesos for farming
        if len(farming) > 0:
            farming = [element["mesos"] for element in farming]
            farming_total = reduce(lambda a, b: a + b, farming)
        else:
            farming_total = 0

        # Update the newly weekly_mesos for this week with the new ursus, tour and farming totals
        WeeklyMesos.query.filter(
            WeeklyMesos.username == data["username"],
            WeeklyMesos.first_day_of_bossing_week == first_day_of_bossing_week).update(
            {"ursus": ursus_total, "tour": tour_total, "farming": farming_total})
        db.session.commit()

        # Query again for the newly updated Weekly Mesos entry for this week
        weekly_mesos = weekly_mesos_schema.dump(
            WeeklyMesos.query.filter(
                WeeklyMesos.username == data["username"],
                WeeklyMesos.first_day_of_bossing_week == first_day_of_bossing_week), many=True)

        # Return response
        response = {
            "message": "Got weekly mesos",
            "weekly_mesos": weekly_mesos[0]
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting farming"
        }
        return jsonify(response), 400


# Update Weekly Mesos
@weekly_mesos_blueprint.patch("/weekly-mesos/update")
def update_weekly_mesos():
    json_data = request.get_json()

    try:
        data = weekly_mesos_schema.load(json_data)

        WeeklyMesos.query.filter(WeeklyMesos.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Weekly mesos is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating weekly mesos"
        }
        return jsonify(response), 400
