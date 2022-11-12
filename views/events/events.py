from app import db
from flask import request, jsonify, Blueprint
from models.users.Users import Users, users_schema
from models.events.EventsMain import EventsMain, events_main_schema
from models.events.EventsSub import EventsSub, events_sub_schema
from models.events.EventsWorldShops import EventsWorldShops, events_world_shops_schema
from models.events.EventsCharacterShops import EventsCharacterShops, events_character_shops_schema
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
        if json_data["event_has_changed"]:
            # Event has changed since the last time the user logged in. Delete all data on the previous event
            UserWorldCurrency.query.filter(UserWorldCurrency.username == json_data["username"]).delete()
            db.session.commit()

        # Query for the user's world currency data
        world_currency = user_world_currency_schema.dump(UserWorldCurrency.query.filter(
            UserWorldCurrency.username == json_data["username"]), many=True)

        if len(world_currency) == 0:
            # This is either a new account, or the event has changed and the previous data has just been deleted
            # Query for world shops and extract distinct values of "currency"
            currencies = events_world_shops_schema.dump(EventsWorldShops.query.filter(
                EventsWorldShops.region == json_data["role"]).with_entities(EventsWorldShops.currency).distinct(),
                                                        many=True)

            # List comprehension to generate a list of object instances to be added to the database
            new_world_currency = [UserWorldCurrency(
                username=json_data["username"], currency=element["currency"]) for element in currencies]

            db.session.add_all(new_world_currency)
            db.session.commit()

            # Query for the newly created data to add to the response
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
@events_blueprint.patch("/events/world/currency/update")
def update_world_currency():
    json_data = request.get_json()

    try:
        data = user_world_currency_schema.load(json_data)

        UserWorldCurrency.query.filter(UserWorldCurrency.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "World currency is updated"
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating world currency"
        }
        return jsonify(response), 400


# Get World Shop Items
@events_blueprint.post("/events/world/shops/get")
def get_world_shops():
    json_data = request.get_json()

    try:
        if json_data["event_has_changed"]:
            # Event has changed since the last time the user logged in. Delete all data on the previous event
            UserWorldShops.query.filter(UserWorldShops.username == json_data["username"]).delete()
            db.session.commit()

        # Query for the user's world shops data
        world_shops = user_world_shops_schema.dump(UserWorldShops.query.filter(
            UserWorldShops.username == json_data["username"]), many=True)

        if len(world_shops) == 0:
            # This is either a new account, or the event has changed and the previous data has just been deleted
            # Query for world shops
            world_shops = events_world_shops_schema.dump(EventsWorldShops.query.all(), many=True)

            # List comprehension to generate a list of object instances to be added to the database
            new_world_shops = [UserWorldShops(
                username=json_data["username"], currency=element["currency"], item=element["item"],
                cost=element["cost"], quantity=element["quantity"]) for element in world_shops]

            db.session.add_all(new_world_shops)
            db.session.commit()

            # Query for the newly created data to add to the response
            world_shops = user_world_shops_schema.dump(UserWorldShops.query.filter(
                UserWorldShops.username == json_data["username"]), many=True)

        response = {
            "message": "Got world shop items",
            "world_shops": world_shops
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting world shop items"
        }
        return jsonify(response), 400


# Update World Shop Item
@events_blueprint.patch("/events/world/shops/update")
def update_world_shop():
    json_data = request.get_json()

    try:
        data = user_world_shops_schema.load(json_data)

        UserWorldShops.query.filter(UserWorldShops.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "World shop item is updated"
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating world shop item"
        }
        return jsonify(response), 400


# Get Character Currency
@events_blueprint.post("/events/character/currency/get")
def get_character_currency():
    json_data = request.get_json()

    try:
        if json_data["event_has_changed"]:
            # Event has changed since the last time the user logged in. Delete all data on the previous event
            UserCharacterCurrency.query.filter(UserCharacterCurrency.character == json_data["character"]).delete()
            db.session.commit()

        # Query for the user's character currency data
        character_currency = user_character_currency_schema.dump(UserCharacterCurrency.query.filter(
            UserCharacterCurrency.username == json_data["username"]), many=True)

        if len(character_currency) == 0:
            # This is either a new account, or the event has changed and the previous data has just been deleted
            # Query for character shops and extract distinct values of "currency"
            currencies = events_character_shops_schema.dump(EventsCharacterShops.query.filter(
                EventsCharacterShops.region == json_data["role"]).with_entities(
                EventsCharacterShops.currency).distinct(), many=True)

            # List comprehension to generate a list of object instances to be added to the database
            new_character_currency = [UserCharacterCurrency(
                character=json_data["character"], currency=element["currency"]) for element in currencies]

            db.session.add_all(new_character_currency)
            db.session.commit()

            # Query for the newly created data to add to the response
            character_currency = user_character_currency_schema.dump(UserCharacterCurrency.query.filter(
                UserCharacterCurrency.username == json_data["username"]), many=True)

        response = {
            "message": "Got character currency",
            "character_currency": character_currency
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting character currency"
        }
        return jsonify(response), 400


# Update Character Currency
@events_blueprint.patch("/events/character/currency/update")
def update_character_currency():
    json_data = request.get_json()

    try:
        data = user_character_currency_schema.load(json_data)

        UserCharacterCurrency.query.filter(UserCharacterCurrency.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Character currency is updated"
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating character currency"
        }
        return jsonify(response), 400


# Get Character Shop Items
@events_blueprint.post("/events/character/shops/get")
def get_character_shops():
    json_data = request.get_json()

    try:
        if json_data["event_has_changed"]:
            # Event has changed since the last time the user logged in. Delete all data on the previous event
            UserCharacterShops.query.filter(UserCharacterShops.character == json_data["character"]).delete()
            db.session.commit()

        # Query for the user's character shops data
        character_shops = user_character_shops_schema.dump(UserCharacterShops.query.filter(
            UserCharacterShops.character == json_data["character"]), many=True)

        if len(character_shops) == 0:
            # This is either a new account, or the event has changed and the previous data has just been deleted
            # Query for character shops
            character_shops = events_character_shops_schema.dump(EventsCharacterShops.query.all(), many=True)

            # List comprehension to generate a list of object instances to be added to the database
            new_character_shops = [UserCharacterShops(
                character=json_data["character"], currency=element["currency"], item=element["item"],
                cost=element["cost"], quantity=element["quantity"]) for element in character_shops]

            db.session.add_all(new_character_shops)
            db.session.commit()

            # Query for the newly created data to add to the response
            character_shops = user_character_shops_schema.dump(UserCharacterShops.query.filter(
                UserCharacterShops.character == json_data["character"]), many=True)

        response = {
            "message": "Got character shop items",
            "character_shops": character_shops
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting character shop items"
        }
        return jsonify(response), 400


# Update Character Shop Item
@events_blueprint.patch("/events/character/shops/update")
def update_character_shop():
    json_data = request.get_json()

    try:
        data = user_character_shops_schema.load(json_data)

        UserCharacterShops.query.filter(UserCharacterShops.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Character shop item is updated"
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating character shop item"
        }
        return jsonify(response), 400
