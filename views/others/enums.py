from flask import jsonify, Blueprint
from models.others.Enums import Roles
from models.others.Enums import Classes
from models.others.Enums import Tracking


views_enums_blueprint = Blueprint("views_enums", __name__)


# Get Roles
@views_enums_blueprint.get("/enums/roles/get")
def get_roles():
    try:
        roles = Roles.query.all()
        roles = [element.roles for element in roles]

        response = {
            "message": "Got roles",
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
            "message": "Got classes",
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
            "message": "Got tracking",
            "tracking": tracking
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting tracking enum"
        }
        return jsonify(response), 400
