from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Dailies(db.Model):
    __tablename__ = "dailies"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    date = db.Column(db.DATE)
    is_prev_day = db.Column(db.BOOLEAN, default=False)
    dailies_list = db.Column(db.TEXT)
    dailies_done = db.Column(db.TEXT, default="")

    def __init__(self, character, date, dailies_list):
        self.character = character
        self.date = date
        self.dailies_list = dailies_list


class DailiesSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    date = fields.Date()
    is_prev_day = fields.Bool()
    dailies_list = fields.Str()
    dailies_done = fields.Str()


dailies_schema = DailiesSchema()
