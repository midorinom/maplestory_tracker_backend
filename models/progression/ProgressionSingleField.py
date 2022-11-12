from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class ProgressionSingleField(db.Model):
    __tablename__ = "progression_single_field"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    slot = db.Column(db.VARCHAR(20), db.ForeignKey("slots_enum.slots"))
    name = db.Column(db.VARCHAR(30), default=None)
    value = db.Column(db.SMALLINT, default=0)

    def __init__(self, character, slot):
        self.character = character
        self.slot = slot


class ProgressionSingleFieldSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    slot = fields.Str()
    name = fields.Str()
    value = fields.Int()


progression_single_field_schema = ProgressionSingleFieldSchema()
