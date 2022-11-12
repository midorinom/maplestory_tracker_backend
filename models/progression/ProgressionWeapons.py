from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class ProgressionWeapons(db.Model):
    __tablename__ = "progression_weapons"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    name = db.Column(db.VARCHAR(30), db.ForeignKey("item_names_enum.item_names"))
    starforce = db.Column(db.SMALLINT, default=0)
    pot_att = db.Column(db.SMALLINT, default=0)
    pot_boss = db.Column(db.SMALLINT, default=0)
    pot_ied = db.Column(db.SMALLINT, default=0)
    pot_mainstat = db.Column(db.SMALLINT, default=0)
    pot_allstats = db.Column(db.SMALLINT, default=0)
    flame_att = db.Column(db.SMALLINT, default=0)
    flame_boss = db.Column(db.SMALLINT, default=0)
    flame_dmg = db.Column(db.SMALLINT, default=0)
    flame_allstats = db.Column(db.SMALLINT, default=0)
    flame_mainstat = db.Column(db.SMALLINT, default=0)

    def __init__(self, character, name):
        self.character = character
        self.name = name


class ProgressionWeaponsSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    name = fields.Str()
    starforce = fields.Int()
    pot_att = fields.Int()
    pot_boss = fields.Int()
    pot_ied = fields.Int()
    pot_mainstat = fields.Int()
    pot_allstats = fields.Int()
    flame_att = fields.Int()
    flame_boss = fields.Int()
    flame_dmg = fields.Int()
    flame_allstats = fields.Int()
    flame_mainstat = fields.Int()


progression_weapons_schema = ProgressionWeaponsSchema()
