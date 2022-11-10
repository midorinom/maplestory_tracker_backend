from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Weeklies(db.Model):
    __tablename__ = "weeklies"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    week = db.Column(db.SMALLINT)
    is_prev_week = db.Column(db.BOOLEAN, default=False)
    weeklies_list = db.Column(db.TEXT)
    weeklies_done = db.Column(db.TEXT)

    def __init__(self, character, week, weeklies_list, weeklies_done):
        self.character = character
        self.week = week
        self.weeklies_list = weeklies_list
        self.weeklies_done = weeklies_done


class WeekliesSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    week = fields.Int()
    is_prev_week = fields.Bool()
    weeklies_list = fields.Str()
    weeklies_done = fields.Str()


weeklies_schema = WeekliesSchema()
