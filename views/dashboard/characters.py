from app import app, db
import os
from flask import request, jsonify, Blueprint, redirect, url_for
from models.dashboard.Characters import Characters, characters_schema
from models.users.Users import Users
from werkzeug.utils import secure_filename

characters_blueprint = Blueprint("characters", __name__)

# Handling Uploads
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000  # 10MB limit


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            new_character = Characters(username=data["username"],
                                       class_name=(data["class_name"]).upper(), ign=data["ign"], level=data["level"])
            db.session.add(new_character)
            db.session.commit()

            # Query for the newly added character
            character = characters_schema.dump(Characters.query.join(Users).filter(
                               Characters.username == data["username"], Characters.ign == data["ign"]), many=True)

            response = {
                "message": "Character is created",
                "character": character[0]
             }
            return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when creating a new character"
        }
        return jsonify(response), 400


# Upload Image
@characters_blueprint.post("/characters/upload/<char_uuid>")
def upload_image(char_uuid):
    try:
        print("files", request.files)
        if 'file' not in request.files:
            print("here1")
            image = None
        else:
            file = request.files['file']
            if file.filename == '':
                print("here2")
                image = None
            if file and allowed_file(file.filename):
                print("here3")
                # Save the image to flask
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))

                # Read the image file and then insert into the database
                data = request.files['file'].read()
                Characters.query.filter(Characters.uuid == char_uuid).update({"image": data})
                db.session.commit()

                # Delete from flask
                os.remove(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))

        response = {
             "message": "Image is uploaded",
         }
        return jsonify(response), 200

    except Exception as err:
        print(err)
        response = {
            "message": "an error has occured when uploading the image"
        }
        return jsonify(response), 400


# Get All Characters
@characters_blueprint.post("/characters/get/all")
def get_all_characters():
    json_data = request.get_json()

    try:
        data = characters_schema.load(json_data)

        characters = characters_schema.dump(Characters.query.order_by(Characters.level.desc()).filter(
            Characters.username == data["username"]), many=True)

        main = characters_schema.dump(Characters.query.filter(Characters.is_main == True), many=True)
        if len(main) > 0:
            main = main[0]

            # Get a new characters list without the main character
            characters_filtered = [character for character in characters if character["is_main"] == False]
            characters = characters_filtered
        else:
            main = None

        response = {
            "message": "Got characters",
            "characters": characters,
            "main": main
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting characters"
        }
        return jsonify(response), 400


# Update Character
@characters_blueprint.patch("/characters/update")
def update_character():
    json_data = request.get_json()

    try:
        data = characters_schema.load(json_data)

        Characters.query.filter(Characters.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Character is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating the character"
        }
        return jsonify(response), 400


# Delete Character
@characters_blueprint.delete("/characters/delete")
def delete_character():
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
