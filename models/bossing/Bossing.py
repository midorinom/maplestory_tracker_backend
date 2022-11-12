from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Bossing(db.Model):
    __tablename__ = "bossing"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    first_day_of_bossing_week = db.Column(db.DATE)
    is_current_week = db.Column(db.BOOLEAN, default=True)
    bossing_list = db.Column(db.TEXT)
    bossing_done = db.Column(db.TEXT, default="")

    def __init__(self, character, first_day_of_bossing_week, bossing_list):
        self.character = character
        self.first_day_of_bossing_week = first_day_of_bossing_week
        self.bossing_list = bossing_list


class BossingSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    first_day_of_bossing_week = fields.Date()
    is_current_week = fields.Bool()
    bossing_list = fields.Str()
    bossing_done = fields.Str()


bossing_schema = BossingSchema()
