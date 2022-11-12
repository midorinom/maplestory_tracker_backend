from app import db
from flask import request, jsonify, Blueprint
from models.progression.ProgressionGear import ProgressionGear, progression_gear_schema
from models.progression.ProgressionOneField import ProgressionOneField, progression_one_field_schema
from models.progression.ProgressionSecondaryEmblem import \
    ProgressionSecondaryEmblem, progression_secondary_emblem_schema
from models.progression.ProgressionWeapons import ProgressionWeapons, progression_weapons_schema

progression_blueprint = Blueprint("progression", __name__)


# Get Progression Gear
@progression_blueprint.post("/progression/gear/get")
def get_progression_gear():
    json_data = request.get_json()

    try:
        # Check if there are existing entries. If there is none, make new entries for this character
        progression_gear = progression_gear_schema.dump(ProgressionGear.query.filter(
            ProgressionGear.character == json_data["character"]
        ), many=True)

        print("here")

        if len(progression_gear) == 0:
            # Define the slots
            slots = ["BELT", "HAT", "FACE", "EYE", "TOP", "BOTTOM", "SHOES",
                     "EARRINGS", "SHOULDER", "GLOVES", "BADGE", "CAPE", "HEART"]
            for i in range(1, 5, 1):
                slots.append("RING" + str(i))
            for i in range(1, 3, 1):
                slots.append("PENDANT" + str(i))

            # Make the new entries and insert them into the database
            new_progression_gear = []
            for slot in slots:
                new_progression_gear.append(ProgressionGear(character=json_data["character"], slot=slot))

            db.session.add_all(new_progression_gear)
            db.session.commit()

            # Query again for the newly added entries to add to the response
            progression_gear = progression_gear_schema.dump(ProgressionGear.query.filter(
                ProgressionGear.character == json_data["character"]
            ), many=True)

        # Return response
        response = {
            "message": "Got progression gear",
            "progression_gear": progression_gear
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting progression gear"
        }
        return jsonify(response), 400


# Update Progression Gear
@progression_blueprint.patch("/progression/gear/update")
def update_progression_gear():
    json_data = request.get_json()

    try:
        data = progression_gear_schema.load(json_data)

        ProgressionGear.query.filter(ProgressionGear.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Progression gear is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating progression gear"
        }
        return jsonify(response), 400
