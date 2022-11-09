from app import db
from flask import request, jsonify, Blueprint
from models.users.Characters import Characters, characters_schema
from models.users.Users import Users


characters_blueprint = Blueprint("characters", __name__)


# Create Character
@characters_blueprint.post("/characters/create")
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
