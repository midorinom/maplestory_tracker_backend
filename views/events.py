from app import db
from flask import request, jsonify, Blueprint
from models.users.Users import Users, users_schema
from models.events.EventsMain import EventsMain, events_main_schema
from models.events.EventsSub import EventsSub, events_sub_schema
from models.events.UserShops import UserWorldShops, UserCharacterShops,\
    user_world_shops_schema, user_character_shops_schema
from models.events.UserCurrency import UserWorldCurrency, UserCharacterCurrency,\
    user_world_currency_schema, user_character_currency_schema


events_blueprint = Blueprint("events", __name__)


# Get Main Event
@events_blueprint.post("/events/main/get")
def get_main_event():
    json_data = request.get_json()

    try:
        # Query for the current main event
        main_event = events_main_schema.dump(EventsMain.query.filter(
            EventsMain.region == json_data["role"]), many=True)
        main_event_name = main_event[0]["name"]

        # Prepare the response
        response = {
            "message": "Got main event",
            "main_event": main_event,
            "event_has_changed": False
        }

        # Query for the event tied to the user
        user = users_schema.dump(Users.query.filter(Users.username == json_data["username"]), many=True)
        user_event = user[0]["event"]

        # If the event tied to the user is the same as the current main event, do nothing and just return the response
        # Otherwise, do the following
        if user_event != main_event_name:
            if user_event is None:
                # It is a new account
                pass
            else:
                # The event has changed since the last time the user logged in
                response["event_has_changed"] = True

            # Add the current event to the user's data
            Users.query.filter(Users.username == json_data["username"]).update({"event": main_event_name})
            db.session.commit()

        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting main event"
        }
        return jsonify(response), 400


# Get Sub Events
@events_blueprint.post("/events/sub/get")
def get_sub_events():
    json_data = request.get_json()

    try:
        sub_events = events_sub_schema.dump(EventsSub.query.filter(EventsSub.region == json_data["role"]), many=True)

        response = {
            "message": "Got sub events",
            "sub_events": sub_events
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting sub events"
        }
        return jsonify(response), 400


# Get World Currency
@events_blueprint.post("/events/world/currency/get")
def get_world_currency():
    json_data = request.get_json()

    try:
        world_currency = user_world_currency_schema.dump(UserWorldCurrency.query.filter(
            UserWorldCurrency.username == json_data["username"]), many=True)

        response = {
            "message": "Got world currency",
            "world_currency": world_currency
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting world currency"
        }
        return jsonify(response), 400


# Update World Currency
@events_blueprint.post("/events/world/currency/update")
def update_world_currency():
    json_data = request.get_json()

    try:
        world_currency = user_world_currency_schema.dump(UserWorldCurrency.query.filter(
            UserWorldCurrency.username == json_data["username"]), many=True)

        response = {
            "message": "Got world currency",
            "world_currency": world_currency
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting world currency"
        }
        return jsonify(response), 400