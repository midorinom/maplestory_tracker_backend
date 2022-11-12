from app import db
from flask import request, jsonify, Blueprint
from models.events.EventsMain import EventsMain, events_main_schema
from models.events.EventsSub import EventsSub, events_sub_schema
from models.events.EventsWorldShops import EventsWorldShops, events_world_shops_schema
from models.events.EventsCharacterShops import EventsCharacterShops, events_character_shops_schema


events_admin_blueprint = Blueprint("events_admin", __name__)


# Get Event Information
@events_admin_blueprint.post("/events-admin/get")
def get_event_information():
    json_data = request.get_json()

    try:
        # Use region as a filter
        main_event = events_main_schema.dump(EventsMain.query.filter(
            EventsMain.region == json_data["region"]), many=True)
        sub_events = events_sub_schema.dump(EventsSub.query.filter(EventsSub.region == json_data["region"]), many=True)
        world_shops = events_world_shops_schema.dump(EventsWorldShops.query.filter(
            EventsWorldShops.region == json_data["region"]), many=True)
        character_shops = events_character_shops_schema.dump(EventsCharacterShops.query.filter(
            EventsCharacterShops.region == json_data["region"]), many=True)

        response = {
            "message": "Got event information",
            "main_event": main_event,
            "sub_events": sub_events,
            "world_shops": world_shops,
            "character_shops": character_shops
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting event information"
        }
        return jsonify(response), 400


# Update Main Event
@events_admin_blueprint.patch("/events-admin/main/update")
def update_main_event():
    json_data = request.get_json()

    try:
        data = events_main_schema.load(json_data)

        EventsMain.query.filter(EventsMain.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Main event is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating main event"
        }
        return jsonify(response), 400


# Add Sub Event
@events_admin_blueprint.put("/events-admin/sub/add")
def add_sub_event():
    json_data = request.get_json()

    try:
        data = events_sub_schema.load(json_data)

        new_sub_event = EventsSub(
            region=data["region"], name=data["name"], start_date=data["start_date"], end_date=data["end_date"])
        db.session.add(new_sub_event)
        db.session.commit()

        response = {
             "message": "Sub event is added",
         }
        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when adding sub event"
        }
        return jsonify(response), 400


# Update Sub Event
@events_admin_blueprint.patch("/events-admin/sub/update")
def update_sub_event():
    json_data = request.get_json()

    try:
        data = events_sub_schema.load(json_data)

        EventsSub.query.filter(EventsSub.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Sub event is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating sub event"
        }
        return jsonify(response), 400


# Delete Sub Event
@events_admin_blueprint.delete("/events-admin/sub/delete")
def delete_sub_event():
    json_data = request.get_json()

    try:
        data = events_sub_schema.load(json_data)

        EventsSub.query.filter(EventsSub.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "Sub event is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the sub event"
        }
        return jsonify(response), 400


# Add World Shop Item
@events_admin_blueprint.put("/events-admin/world/add")
def add_world_shop():
    json_data = request.get_json()

    try:
        data = events_world_shops_schema.load(json_data)

        new_world_shop = EventsWorldShops(
            region=data["region"], currency=data["currency"], item=data["item"], cost=data["cost"],
            quantity=data["quantity"])
        db.session.add(new_world_shop)
        db.session.commit()

        response = {
             "message": "World shop item is added",
         }
        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when adding world shop item"
        }
        return jsonify(response), 400


# Update World Shop Item
@events_admin_blueprint.patch("/events-admin/world/update")
def update_world_shop():
    json_data = request.get_json()

    try:
        data = events_world_shops_schema.load(json_data)

        EventsWorldShops.query.filter(EventsWorldShops.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "World shop item is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating world shop item"
        }
        return jsonify(response), 400


# Delete World Shop Item
@events_admin_blueprint.delete("/events-admin/world/delete")
def delete_world_shop():
    json_data = request.get_json()

    try:
        data = events_world_shops_schema.load(json_data)

        EventsWorldShops.query.filter(EventsWorldShops.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "World shop item is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the world shop item"
        }
        return jsonify(response), 400


# Add Character Shop Item
@events_admin_blueprint.put("/events-admin/character/add")
def character():
    json_data = request.get_json()

    try:
        data = events_character_shops_schema.load(json_data)

        new_character_shop = EventsCharacterShops(
            region=data["region"], currency=data["currency"], item=data["item"], cost=data["cost"],
            quantity=data["quantity"])
        db.session.add(new_character_shop)
        db.session.commit()

        response = {
             "message": "Character shop item is added",
         }
        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when adding character shop item"
        }
        return jsonify(response), 400


# Update Character Shop Item
@events_admin_blueprint.patch("/events-admin/character/update")
def update_character_shop():
    json_data = request.get_json()

    try:
        data = events_character_shops_schema.load(json_data)

        EventsCharacterShops.query.filter(EventsCharacterShops.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Character shop item is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating character shop item"
        }
        return jsonify(response), 400


# Delete Character Shop Item
@events_admin_blueprint.delete("/events-admin/character/delete")
def delete_character_shop():
    json_data = request.get_json()

    try:
        data = events_character_shops_schema.load(json_data)

        EventsCharacterShops.query.filter(EventsCharacterShops.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "Character shop item is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the character shop item"
        }
        return jsonify(response), 400
