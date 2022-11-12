from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class ProgressionSecondaryEmblem(db.Model):
    __tablename__ = "progression_secondary_emblem"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    slot = db.Column(db.VARCHAR(20), db.ForeignKey("slots_enum.slots"))
    name = db.Column(db.VARCHAR(30), default=None)
    starforce = db.Column(db.SMALLINT, default=0)
    pot_att = db.Column(db.SMALLINT, default=0)
    pot_boss = db.Column(db.SMALLINT, default=0)
    pot_ied = db.Column(db.SMALLINT, default=0)
    pot_mainstat = db.Column(db.SMALLINT, default=0)
    pot_allstats = db.Column(db.SMALLINT, default=0)

    def __init__(self, character, slot):
        self.character = character
        self.slot = slot


class ProgressionSecondaryEmblemSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    slot = fields.Str()
    name = fields.Str()
    starforce = fields.Int()
    pot_att = fields.Int()
    pot_boss = fields.Int()
    pot_ied = fields.Int()
    pot_mainstat = fields.Int()
    pot_allstats = fields.Int()


progression_secondary_emblem_schema = ProgressionSecondaryEmblemSchema()
