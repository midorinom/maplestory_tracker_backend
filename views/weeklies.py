from app import db
from flask import request, jsonify, Blueprint
from models.dailies.Weeklies import Weeklies, weeklies_schema
import datetime


weeklies_blueprint = Blueprint("weeklies", __name__)


# Get Weeklies
@weeklies_blueprint.post("/weeklies/get")
def get_dailies():
    json_data = request.get_json()

    try:
        # Convert from date to week
        date_list = json_data["date"].split("-")
        date_list = [int(i) for i in date_list]
        date = datetime.date(*date_list)
        week = date.isocalendar().week

        # Change key in json_data from "date" to "week", then load json_data
        json_data["week"] = json_data.pop("date")
        json_data["week"] = week

        data = weeklies_schema.load(json_data)

        # Response object
        response = {
            "message": "Got weeklies",
        }

        # Check if there is an existing entry for this week. If so, add it to the response
        weeklies = weeklies_schema.dump(Weeklies.query.filter(Weeklies.character == data["character"],
                                                              Weeklies.week == week), many=True)

        if len(weeklies) > 0:
            response["weeklies"] = weeklies[0]
        else:
            # Look up the existing entries
            existing_weeklies = weeklies_schema.dump(Weeklies.query.filter(Weeklies.character == data["character"]),
                                                     many=True)

            # Index will be 0 if there is only 1 existing entry
            index = 0

            if len(existing_weeklies) == 2:
                # There are 2 existing entries. If the second element is the latest entry, set index to 1
                if existing_weeklies[1]["week"] > existing_weeklies[0]["week"]:
                    index = 1

                # Delete the older entry
                Weeklies.query.filter(Weeklies.uuid == existing_weeklies[0 if index == 1 else 1]["uuid"]).delete()
                db.session.commit()

            # If there are existing entries, set the latest existing entry to is_prev_week=True
            if len(existing_weeklies) > 0:
                Weeklies.query.filter(Weeklies.uuid == existing_weeklies[index]["uuid"]).update({"is_prev_week": True})
                db.session.commit()

            # Make an entry for this week
            new_weeklies = Weeklies(character=data["character"], week=week,
                                    weeklies_list="test1@test2@test3", weeklies_done="test1@test2")
            db.session.add(new_weeklies)
            db.session.commit()
            response["weeklies"] = weeklies_schema.dump(new_weeklies)

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
