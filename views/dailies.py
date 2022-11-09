from app import db
from flask import request, jsonify, Blueprint
from models.dailies.Dailies import Dailies, dailies_schema


dailies_blueprint = Blueprint("dailies", __name__)


# Create Character
@dailies_blueprint.post("/characters/create")
def create_character():
    json_data = request.get_json()

    try:
        data = characters_schema.load(json_data)

        # Check if the same character has already been created by this user
        duplicate_character = characters_schema.dump(Characters.query.join(Users).filter(
                               Characters.username == data["username"], Characters.ign == data["ign"]), many=True)
        if duplicate_character:
            response = {
                "message": "This character has already been created"
            }
            return jsonify(response), 400

        else:
            new_character = Characters(username=data["username"], class_name=data["class_name"], ign=data["ign"],
                                       level=data["level"])
            db.session.add(new_character)
            db.session.commit()

            response = {
                "message": "Character is created",
             }
            return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when creating a new character"
        }
        return jsonify(response), 400


# Get All Characters
@characters_blueprint.post("/characters/get/all")
def get_all_characters():
    json_data = request.get_json()

    try:
        data = characters_schema.load(json_data)

        all_characters = characters_schema.dump(Characters.query.filter(Characters.username == data["username"]),
                                                many=True)

        response = {
            "message": "Got all characters",
            "all_characters": all_characters
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting all characters"
        }
        return jsonify(response), 400


# Delete Character
@characters_blueprint.delete("/characters/delete")
def delete_characters():
    json_data = request.get_json()

    try:
        data = characters_schema.load(json_data)

        Characters.query.filter(Characters.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "Character is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the character"
        }
        return jsonify(response), 400
