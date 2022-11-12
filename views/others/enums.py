from flask import jsonify, Blueprint
from models.others.Enums import Roles
from models.others.Enums import Classes
from models.others.Enums import Tracking
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
@views_enums_blueprint.get("/enums/classes/get")
def get_classes():
    try:
        classes = Classes.query.all()
        classes = [element.classes for element in classes]

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


# Get Tracking
@views_enums_blueprint.get("/enums/tracking/get")
def get_tracking():
    try:
        tracking = Tracking.query.all()
        tracking = [element.tracking for element in tracking]

        response = {
            "message": "Got tracking enum",
            "tracking": tracking
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting tracking enum"
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


# Get Item Names
@views_enums_blueprint.get("/enums/item-names/get")
def get_item_names():
    try:
        item_names = ItemNames.query.all()
        item_names = [element.item_names for element in item_names]

        response = {
            "message": "Got item names enum",
            "item_names": item_names
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting item names enum"
        }
        return jsonify(response), 400