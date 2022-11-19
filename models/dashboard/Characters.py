from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class Characters(db.Model):
    __tablename__ = "characters"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username"))
    class_name = db.Column(db.VARCHAR(20), db.ForeignKey("classes_enum.classes"))
    ign = db.Column(db.VARCHAR(12))
    level = db.Column(db.SMALLINT)
    tracking = db.Column(db.VARCHAR(60), default="dailies@bossing@progression@farming@events")
    is_main = db.Column(db.BOOLEAN, default=False)
    stats = db.Column(db.INT, nullable=True)
    dojo = db.Column(db.SMALLINT, nullable=True)
    ba = db.Column(db.SMALLINT, nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    dailies = relationship("Dailies", backref="characters", passive_deletes=True)
    weeklies = relationship("Weeklies", backref="characters", passive_deletes=True)

    def __init__(self, username, class_name, ign, level):
        self.username = username
        self.class_name = class_name
        self.ign = ign
        self.level = level


class CharactersSchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    class_name = fields.Str()
    ign = fields.Str()
    level = fields.Int()
    tracking = fields.Str()
    is_main = fields.Bool()
    stats = fields.Int(allow_none=True)
    dojo = fields.Int(allow_none=True)
    ba = fields.Int(allow_none=True)
    image = fields.Raw(allow_none=True)


characters_schema = CharactersSchema()
