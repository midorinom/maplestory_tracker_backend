from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Weeklies(db.Model):
    __tablename__ = "weeklies"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    week_starting_from = db.Column(db.DATE)
    is_prev_week = db.Column(db.BOOLEAN)
    weeklies_list = db.Column(db.VARCHAR(50))
    weeklies_done = db.Column(db.VARCHAR(50))

    def __init__(self, character, week_starting_from, is_prev_week, weeklies_list, weeklies_done):
        self.character = character
        self.date = week_starting_from
        self.is_prev_week = is_prev_week
        self.weeklies_list = weeklies_list
        self.weeklies_done = weeklies_done


class WeekliesSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    week_starting_from = fields.Date()
    is_prev_week = fields.Bool()
    weeklies_list = fields.Str()
    weeklies_done = fields.Str()


weeklies_schema = WeekliesSchema()
