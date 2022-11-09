from app import db
from flask import request, jsonify, Blueprint
from models.dailies.Weeklies import Weeklies, weeklies_schema


weeklies_blueprint = Blueprint("weeklies", __name__)
