from app import db
from flask import request, jsonify, Blueprint
from models.users.Legion import Legion, legion_schema


legion_blueprint = Blueprint("legion", __name__)


# Get Legion
@legion_blueprint.post("/legion/get")
def get_legion():
    json_data = request.get_json()

    try:
        data = legion_schema.load(json_data)

        legion = legion_schema.dump(Legion.query.order_by(
            Legion.level.desc()).filter(
            Legion.username == data["username"]).with_entities(Legion.class_name, Legion.level), many=True)

        response = {
            "message": "Got legion",
            "legion": legion
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting legion"
        }
        return jsonify(response), 400


# Add Legion Character
@legion_blueprint.put("/legion/add")
def add_legion():
    json_data = request.get_json()

    try:
        data = legion_schema.load(json_data)

        new_legion = Legion(username=data["username"], class_name=data["class_name"], level=data["level"])
        db.session.add(new_legion)
        db.session.commit()

        response = {
             "message": "Legion character is added",
         }
        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when adding legion character"
        }
        return jsonify(response), 400


# Update Legion Character
@legion_blueprint.patch("/legion/update")
def update_legion():
    json_data = request.get_json()

    try:
        data = legion_schema.load(json_data)

        Legion.query.filter(Legion.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Legion character is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating legion character"
        }
        return jsonify(response), 400


# Delete Legion Character
@legion_blueprint.delete("/legion/delete")
def delete_legion():
    json_data = request.get_json()

    try:
        data = legion_schema.load(json_data)

        Legion.query.filter(Legion.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "Legion character is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the legion character"
        }
        return jsonify(response), 400
