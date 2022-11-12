from app import db
from flask import request, jsonify, Blueprint
from models.progression.ProgressionGear import ProgressionGear, progression_gear_schema
from models.progression.ProgressionSecondaryEmblem import \
    ProgressionSecondaryEmblem, progression_secondary_emblem_schema
from models.progression.ProgressionSingleField import ProgressionSingleField, progression_single_field_schema
from models.progression.ProgressionWeapons import ProgressionWeapons, progression_weapons_schema
from models.progression.Items import Items, items_schema

progression_blueprint = Blueprint("progression", __name__)


# Get Gear
@progression_blueprint.post("/progression/gear/get")
def get_gear():
    json_data = request.get_json()

    try:
        # Check if there are existing entries. If there is none, make new entries for this character
        gear = progression_gear_schema.dump(ProgressionGear.query.filter(
            ProgressionGear.character == json_data["character"]), many=True)

        if len(gear) == 0:
            # Define the slots
            slots = ["BELT", "HAT", "FACE", "EYE", "TOP", "BOTTOM", "SHOES",
                     "EARRINGS", "SHOULDER", "GLOVES", "BADGE", "CAPE", "HEART"]
            for i in range(1, 5, 1):
                slots.append("RING" + str(i))
            for i in range(1, 3, 1):
                slots.append("PENDANT" + str(i))

            # Make the new entries and insert them into the database
            new_gear = [ProgressionGear(character=json_data["character"], slot=slot) for slot in slots]

            db.session.add_all(new_gear)
            db.session.commit()

            # Query again for the newly added entries to add to the response
            gear = progression_gear_schema.dump(ProgressionGear.query.filter(
                ProgressionGear.character == json_data["character"]), many=True)

        # Return response
        response = {
            "message": "Got gear",
            "gear": gear
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting gear"
        }
        return jsonify(response), 400


# Update Gear
@progression_blueprint.patch("/progression/gear/update")
def update_gear():
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
            "message": "Gear is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating gear"
        }
        return jsonify(response), 400


# Get Secondary Emblem
@progression_blueprint.post("/progression/secondary-emblem/get")
def get_secondary_emblem():
    json_data = request.get_json()

    try:
        # Check if there are existing entries. If there is none, make new entries for this character
        secondary_emblem = progression_secondary_emblem_schema.dump(ProgressionSecondaryEmblem.query.filter(
            ProgressionSecondaryEmblem.character == json_data["character"]), many=True)

        if len(secondary_emblem) == 0:
            # Define the slots
            slots = ["SECONDARY", "EMBLEM"]

            # Make the new entries and insert them into the database
            new_secondary_emblem = [ProgressionSecondaryEmblem(
                character=json_data["character"], slot=slot) for slot in slots]

            db.session.add_all(new_secondary_emblem)
            db.session.commit()

            # Query again for the newly added entries to add to the response
            secondary_emblem = progression_secondary_emblem_schema.dump(ProgressionSecondaryEmblem.query.filter(
                ProgressionSecondaryEmblem.character == json_data["character"]), many=True)

        # Return response
        response = {
            "message": "Got secondary emblem",
            "secondary_emblem": secondary_emblem
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting secondary emblem"
        }
        return jsonify(response), 400


# Update Secondary Emblem
@progression_blueprint.patch("/progression/secondary-emblem/update")
def update_secondary_emblem():
    json_data = request.get_json()

    try:
        data = progression_secondary_emblem_schema.load(json_data)

        ProgressionSecondaryEmblem.query.filter(ProgressionSecondaryEmblem.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Secondary emblem is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating secondary emblem"
        }
        return jsonify(response), 400


# Get Single Field Items
@progression_blueprint.post("/progression/single-field/get")
def get_single_field():
    json_data = request.get_json()

    try:
        # Check if there are existing entries. If there is none, make new entries for this character
        single_field = progression_single_field_schema.dump(ProgressionSingleField.query.filter(
            ProgressionSingleField.character == json_data["character"]), many=True)

        if len(single_field) == 0:
            # Define the slots
            slots = ["POCKET", "MEDAL", "TITLE", "SOUL"]

            for i in range(1, 3, 1):
                slots.append("OZ_RING" + str(i))
            for i in range(1, 4, 1):
                slots.append("TOTEM" + str(i))
                slots.append("INNER_ABILITY" + str(i))
                slots.append("GRANDIS_SYMBOL" + str(i))
            for i in range(1, 5, 1):
                slots.append("RING" + str(i))
            for i in range(1, 7, 1):
                slots.append("ARCANE_SYMBOL" + str(i))
                slots.append("FAMILIAR" + str(i))

            # Make the new entries and insert them into the database
            new_single_field = [ProgressionSingleField(
                character=json_data["character"], slot=slot) for slot in slots]

            db.session.add_all(new_single_field)
            db.session.commit()

            # Query again for the newly added entries to add to the response
            single_field = progression_single_field_schema.dump(ProgressionSingleField.query.filter(
                ProgressionSingleField.character == json_data["character"]
            ), many=True)

        # Return response
        response = {
            "message": "Got single field items",
            "single_field": single_field
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting single field items"
        }
        return jsonify(response), 400


# Update Single Field Item
@progression_blueprint.patch("/progression/single-field/update")
def update_single_field():
    json_data = request.get_json()

    try:
        data = progression_single_field_schema.load(json_data)

        ProgressionSingleField.query.filter(ProgressionSingleField.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Single field item is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating single field item"
        }
        return jsonify(response), 400


# Get Weapon
@progression_blueprint.post("/progression/weapon/get")
def get_weapon():
    json_data = request.get_json()

    try:
        # Check if is an existing entry. If there is none, make a new entry for this character
        weapon = progression_weapons_schema.dump(ProgressionWeapons.query.filter(
            ProgressionWeapons.character == json_data["character"]), many=True)

        if len(weapon) == 0:
            # Make the new entry and insert it into the database
            new_weapon = ProgressionWeapons(character=json_data["character"])
            db.session.add(new_weapon)
            db.session.commit()

            # Query again for the newly added entry to add to the response
            weapon = progression_weapons_schema.dump(ProgressionWeapons.query.filter(
                ProgressionWeapons.character == json_data["character"]), many=True)

        # Return response
        response = {
            "message": "Got weapon",
            "weapon": weapon
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting weapon"
        }
        return jsonify(response), 400


# Update Weapon
@progression_blueprint.patch("/progression/weapon/update")
def update_weapon():
    json_data = request.get_json()

    try:
        data = progression_weapons_schema.load(json_data)

        ProgressionWeapons.query.filter(ProgressionWeapons.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Weapon is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating waepon"
        }
        return jsonify(response), 400


# Get Items
@progression_blueprint.post("/progression/items/get")
def get_items():
    json_data = request.get_json()

    try:
        items = items_schema.dump(
            (Items.query.filter(Items.region == json_data["role"], Items.slot == json_data["slot"])), many=True)

        response = {
            "message": "Got items",
            "items": items
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting items"
        }
        return jsonify(response), 400
