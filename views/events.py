from app import db
from flask import request, jsonify, Blueprint
from models.users.Users import Users, users_schema
from models.events.EventsMain import EventsMain, events_main_schema


events_blueprint = Blueprint("events", __name__)


# Get Main Event
@events_blueprint.post("/events/main/get")
def get_main_event():
    json_data = request.get_json()

    try:
        # Query for the current main event
        main_event = events_main_schema.dump(EventsMain.query.filter(
            EventsMain.region == json_data["region"]), many=True)
        if main_event[0]["name"] == "none":
            main_event_uuid = "none"
        else:
            main_event_uuid = main_event[0]["uuid"]

        # Check for the event tied to the user
        user = users_schema.dump(Users.query.filter(Users.username == json_data["username"]), many=True)
        user_event = user[0]["event"]

        if user_event is None:
            # It is a new account. Add the current event to the user's data
            Users.query.filter(Users.username == json_data["username"]).update(
                {"event": main_event_uuid})
            db.session.commit()

        response = {
            "user_event": user_event,
            "main_event": main_event
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting main event"
        }
        return jsonify(response), 400
