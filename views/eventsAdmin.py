from app import db
from flask import request, jsonify, Blueprint
from models.events.EventsMain import EventsMain, events_main_schema
from models.events.EventsSub import EventsSub, events_sub_schema
from models.events.EventsWorldShops import EventsWorldShops, events_world_shops_schema
from models.events.EventsCharacterShops import EventsCharacterShops, events_character_shops_schema


events_admin_blueprint = Blueprint("events_admin", __name__)

#
# # Get Event Information
# @events_admin_blueprint.post("/events-admin/get")
# def get_event_information():
#     json_data = request.get_json()
#
#     try:
#         if json_data["region"] == "MSEA":
#             # Get Maplesea Events
#             main = EventsMainMsea.query.filter({})
#             sub = EventsSubMsea.query.all()
#
#
#         else:
#             # Get Gms Events
#
#         legion = Legion.query.order_by(Legion.level.desc()).filter(Legion.username == data["username"])
#         legion = [{"class_name": element.class_name, "level": element.level} for element in legion]
#
#         response = {
#             "message": "Got legion",
#             "legion": legion
#         }
#         return jsonify(response), 200
#
#     except Exception as err:
#         print(err)
#
#         response = {
#             "message": "an error has occured when getting event information"
#         }
#         return jsonify(response), 400
