from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class ProgressionOneField(db.Model):
    __tablename__ = "progression_one_field"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    slot = db.Column(db.VARCHAR(20), db.ForeignKey("slots_enum.slots"))
    name = db.Column(db.VARCHAR(30), db.ForeignKey("item_names_enum.item_names"))
    value = db.Column(db.SMALLINT, default=0)

    def __init__(self, character, slot, name):
        self.character = character
        self.slot = slot
        self.name = name


class ProgressionOneFieldSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    slot = fields.Str()
    name = fields.Str()
    value = fields.Int()


progression_one_field_schema = ProgressionOneFieldSchema()
