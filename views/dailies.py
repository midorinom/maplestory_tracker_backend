from app import db
from flask import request, jsonify, Blueprint
from models.dailies.Dailies import Dailies, dailies_schema
import datetime
from models.NonRelational import DailiesDefault


dailies_blueprint = Blueprint("dailies", __name__)


# Get Dailies
@dailies_blueprint.post("/dailies/get")
def get_dailies():
    json_data = request.get_json()

    try:
        data = dailies_schema.load(json_data)

        # Response dictionary
        response = {
            "message": "Got dailies",
        }

        # Check if there is an existing entry for today's date. If so, add it to the response
        dailies = dailies_schema.dump(Dailies.query.filter(Dailies.character == data["character"],
                                                           Dailies.date == data["date"]))
        if len(dailies) > 0:
            response["dailies"] = dailies[0]
        else:
            # Look up the existing entries
            existing_dailies = dailies_schema.dump(Dailies.query.filter(Dailies.character == data["character"]))

            # Index will be 0 if there is only 1 existing entry
            index = 0

            if len(existing_dailies) == 2:
                # There are 2 existing entries. Check which one is the latest
                date1_list = existing_dailies[0]["date"].split("-")
                date1_list = [int(i) for i in date1_list]
                date1 = datetime.date(*date1_list)

                date2_list = existing_dailies[1]["date"].split("-")
                date2_list = [int(i) for i in date2_list]
                date2 = datetime.date(*date2_list)

                # If the second element is the latest entry, set index to 1
                if date2 > date1:
                    index = 1

                # Delete the older entry
                Dailies.query.filter(Dailies.uuid == existing_dailies[0 if index == 1 else 1]["uuid"]).delete()
                db.session.commit()

            # If there are existing entries, set the latest entry to is_current_day=False. Also, set dailies_list
            if len(existing_dailies) > 0:
                Dailies.query.filter(Dailies.uuid == existing_dailies[index]["uuid"]).update({"is_current_day": False})
                db.session.commit()

                dailies_list = existing_dailies[index]["dailies_list"]
            else:
                # Query from the dailies_default table and construct a dailies_list from the data
                dailies_default = DailiesDefault.query.all()
                dailies_default = [element.dailies_list for element in dailies_default]
                dailies_list = "@".join(dailies_default)

            # Make an entry for today's date
            new_dailies = Dailies(character=data["character"], date=data["date"],
                                  dailies_list=dailies_list)
            db.session.add(new_dailies)
            db.session.commit()
            response["dailies"] = dailies_schema.dump(new_dailies)

        # Return response
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting dailies"
        }
        return jsonify(response), 400


# Update Dailies
@dailies_blueprint.patch("/dailies/update")
def update_dailies():
    json_data = request.get_json()

    try:
        data = dailies_schema.load(json_data)

        Dailies.query.filter(Dailies.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Dailies is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating dailies"
        }
        return jsonify(response), 400
