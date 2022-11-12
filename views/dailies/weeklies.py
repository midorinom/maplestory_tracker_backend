from app import db
from flask import request, jsonify, Blueprint
from models.dailies.Weeklies import Weeklies, weeklies_schema
import datetime
from models.others.NonRelational import WeekliesDefault


weeklies_blueprint = Blueprint("weeklies", __name__)


# Get Weeklies
@weeklies_blueprint.post("/weeklies/get")
def get_weeklies():
    json_data = request.get_json()

    try:
        # Using today's date, get the first_day_of_week
        date_list = json_data["date"].split("-")
        date_list = [int(i) for i in date_list]
        date = datetime.date(*date_list)

        # timedelta subtracts the current weekday (converted to a value) from today's date, to get Monday's date
        # The operation involving timedelta returns a datetime Object. strftime formats it back to a string
        first_day_of_week = (date + datetime.timedelta(days=-date.weekday())).strftime("%Y-%m-%d")

        # Remove date from json_data, add first_day_of_week, then load json_data
        json_data.pop("date")
        json_data["first_day_of_week"] = first_day_of_week

        data = weeklies_schema.load(json_data)

        # Response dictionary
        response = {
            "message": "Got weeklies",
        }

        # Check if there is an existing entry for this week. If so, add it to the response
        weeklies = weeklies_schema.dump(Weeklies.query.filter(
            Weeklies.character == data["character"], Weeklies.first_day_of_week == first_day_of_week), many=True)

        if len(weeklies) > 0:
            response["weeklies"] = weeklies[0]
        else:
            # Look up the existing entries
            existing_weeklies = weeklies_schema.dump(Weeklies.query.filter(
                Weeklies.character == data["character"]), many=True)

            # Index will be 0 if there is only 1 existing entry
            index = 0

            if len(existing_weeklies) == 2:
                # There are 2 existing entries. Check which one is the latest
                date1_list = existing_weeklies[0]["first_day_of_week"].split("-")
                date1_list = [int(i) for i in date1_list]
                date1 = datetime.date(*date1_list)

                date2_list = existing_weeklies[1]["first_day_of_week"].split("-")
                date2_list = [int(i) for i in date2_list]
                date2 = datetime.date(*date2_list)

                # If the second element is the latest entry, set index to 1
                if date2 > date1:
                    index = 1

                # Delete the older entry
                Weeklies.query.filter(Weeklies.uuid == existing_weeklies[0 if index == 1 else 1]["uuid"]).delete()
                db.session.commit()

            # If there are existing entries, set the latest entry to is_current_week=False. Also, set weeklies_list
            if len(existing_weeklies) > 0:
                Weeklies.query.filter(
                    Weeklies.uuid == existing_weeklies[index]["uuid"]).update({"is_current_week": False})
                db.session.commit()

                weeklies_list = existing_weeklies[index]["weeklies_list"]
            else:
                # Query from the weeklies_default table and construct a dailies_list from the data
                weeklies_default = WeekliesDefault.query.all()
                weeklies_default = [element.weeklies_list for element in weeklies_default]
                weeklies_list = "@".join(weeklies_default)

            # Make an entry for this week
            new_weeklies = Weeklies(character=data["character"], first_day_of_week=first_day_of_week,
                                    weeklies_list=weeklies_list)
            db.session.add(new_weeklies)
            db.session.commit()

            # Query for the newly added entry and add it to the response
            response["weeklies"] = weeklies_schema.dump(
                Weeklies.query.filter(
                    Weeklies.character == data["character"],
                    Weeklies.first_day_of_week == first_day_of_week), many=True)[0]

        # Return response
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting weeklies"
        }
        return jsonify(response), 400


# Update Weeklies
@weeklies_blueprint.patch("/weeklies/update")
def update_weeklies():
    json_data = request.get_json()

    try:
        data = weeklies_schema.load(json_data)

        Weeklies.query.filter(Weeklies.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Weeklies is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating weeklies"
        }
        return jsonify(response), 400
