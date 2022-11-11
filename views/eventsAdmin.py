from app import db
from flask import request, jsonify, Blueprint
from models.users.Legion import Legion, legion_schema


events_admin_blueprint = Blueprint("events_admin", __name__)


# Get
@events_admin_blueprint.post("/events-admin/get")
def get_legion():
    json_data = request.get_json()

    try:
        data = legion_schema.dump(json_data)

        legion = Legion.query.order_by(Legion.level.desc()).filter(Legion.username == data["username"])
        legion = [{"class_name": element.class_name, "level": element.level} for element in legion]

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
