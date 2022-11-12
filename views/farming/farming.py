from app import db
from flask import request, jsonify, Blueprint
from models.farming.Farming import Farming, farming_schema
import datetime


farming_blueprint = Blueprint("farming", __name__)


# Get Farming
@farming_blueprint.post("/farming/get")
def get_farming():
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

        data = farming_schema.load(json_data)

        # Response dictionary
        response = {
            "message": "Got farming",
        }

        # Check if there is are existing entries for this week. If so, add it to the response
        farming = farming_schema.dump(Farming.query.filter(Farming.character == data["character"],
                                                           Farming.first_day_of_week == first_day_of_week), many=True)

        if len(farming) > 0:
            response["farming"] = farming
        else:
            # Change existing entries with is_current_week == True to False
            Farming.query.filter(
                Farming.character == data["character"], Farming.is_current_week == True).update(
                {"is_current_week": False})

            # Make new entries for this week
            new_farming = []
            first_day_of_week = date + datetime.timedelta(days=-date.weekday())
            first_day_of_bossing_week = date + datetime.timedelta(days=-date.weekday()+3)

            loop = range(7)
            for i in loop:
                new_farming.append(
                    Farming(character=data["character"],
                            date=first_day_of_week + datetime.timedelta(days=i),
                            first_day_of_week=first_day_of_week, first_day_of_bossing_week=first_day_of_bossing_week))

            db.session.add_all(new_farming)
            db.session.commit()

            # Query for the newly added entries and add them to the response
            response["farming"] = farming_schema.dump(Farming.query.filter(
                Farming.character == data["character"], Farming.first_day_of_week == first_day_of_week), many=True)

        # Return response
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting farming"
        }
        return jsonify(response), 400


# Update Weeklies
@farming_blueprint.patch("/farming/update")
def update_farming():
    json_data = request.get_json()

    try:
        data = farming_schema.load(json_data)

        Farming.query.filter(Farming.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Farming is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating farming"
        }
        return jsonify(response), 400
