from flask import request, jsonify, Blueprint
from sqlalchemy import or_
from models.others.Enums import Roles
from models.others.Enums import Classes
from models.others.Enums import Slots


views_enums_blueprint = Blueprint("views_enums", __name__)


# Get Roles
@views_enums_blueprint.get("/enums/roles/get")
def get_roles():
    try:
        roles = Roles.query.all()
        roles = [element.roles for element in roles]

        response = {
            "message": "Got roles enum",
            "roles": roles
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting roles enum"
        }
        return jsonify(response), 400


# Get Classes
@views_enums_blueprint.post("/enums/classes/get")
def get_classes():
    json_data = request.get_json()

    try:
        classes = Classes.query.order_by(Classes.classes.asc()).filter(
            or_(Classes.region == json_data["role"], Classes.region == "BOTH"))
        classes = [element.classes.title() for element in classes]

        response = {
            "message": "Got classes enum",
            "classes": classes
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting classes enum"
        }
        return jsonify(response), 400


# Get Slots
@views_enums_blueprint.get("/enums/slots/get")
def get_slots():
    try:
        slots = Slots.query.all()
        slots = [element.slots for element in slots]

        response = {
            "message": "Got slots enum",
            "slots": slots
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting slots enum"
        }
        return jsonify(response), 400
