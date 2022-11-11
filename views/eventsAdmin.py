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
        # Use region as a filter,
        main_events = events_main_schema.dump(EventsMain.query.filter(EventsMain.region == json_data["region"]))
        sub_events = events_sub_schema.dump(EventsSub.query.filter(EventsSub.region == json_data["region"]))
        world_shops = events_world_shops_schema.dump(EventsWorldShops.query.filter(
            EventsWorldShops.region == json_data["region"]))
        character_shops = events_character_shops_schema.dump(EventsCharacterShops.query.filter(
            EventsCharacterShops.region == json_data["region"]))

        print(events_sub_schema.dump(EventsSub.query.filter(EventsSub.region == json_data["region"]), many=True))

        response = {
            "message": "Got event information",
            "main_events": main_events,
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
