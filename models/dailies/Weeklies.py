from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Weeklies(db.Model):
    __tablename__ = "weeklies"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    first_day_of_week = db.Column(db.DATE)
    is_current_week = db.Column(db.BOOLEAN, default=True)
    weeklies_list = db.Column(db.TEXT)
    weeklies_done = db.Column(db.TEXT, default="")

    def __init__(self, character, first_day_of_week, weeklies_list):
        self.character = character
        self.first_day_of_week = first_day_of_week
        self.weeklies_list = weeklies_list


class WeekliesSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    first_day_of_week = fields.Date()
    is_current_week = fields.Bool()
    weeklies_list = fields.Str()
    weeklies_done = fields.Str()


weeklies_schema = WeekliesSchema()
