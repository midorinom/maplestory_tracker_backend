from flask import jsonify, Blueprint
from models.Enums import Classes


views_enums_blueprint = Blueprint("views_enums", __name__)


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
            "message": "an error has occured when getting classes"
        }
        return jsonify(response), 400
