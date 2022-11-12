from app import db
from flask import request, jsonify, Blueprint
from models.dailies.UrsusTour import UrsusTour, ursus_tour_schema

ursus_tour_blueprint = Blueprint("ursus_tour", __name__)


# Get ursus_tour
@ursus_tour_blueprint.post("/ursus-tour/get")
def get_ursus_tour():
    json_data = request.get_json()

    try:
        data = ursus_tour_schema.load(json_data)

        # Response dictionary
        response = {
            "message": "Got ursus_tour",
        }

        # Check if there is an existing entry for today's date. If so, add it to the response
        ursus_tour = ursus_tour_schema.dump(UrsusTour.query.filter(UrsusTour.username == data["username"],
                                                                   UrsusTour.date == data["date"]), many=True)
        if len(ursus_tour) > 0:
            response["ursus_tour"] = ursus_tour[0]
        else:
            # Make a new entry for today's date and add it to the response
            new_ursus_tour = UrsusTour(username=data["username"], date=data["date"])
            db.session.add(new_ursus_tour)
            db.session.commit()

            # Query for the newly added entry and add it to the response
            response["ursus_tour"] = ursus_tour_schema.dump(
                UrsusTour.query.filter(
                    UrsusTour.username == data["username"], UrsusTour.date == data["date"]), many=True)[0]

        # Return response
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting ursus_tour"
        }
        return jsonify(response), 400


# Update ursus_tour
@ursus_tour_blueprint.patch("/ursus-tour/update")
def update_ursus_tour():
    json_data = request.get_json()

    try:
        data = ursus_tour_schema.load(json_data)

        UrsusTour.query.filter(UrsusTour.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "ursus_tour is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating ursus_tour"
        }
        return jsonify(response), 400
