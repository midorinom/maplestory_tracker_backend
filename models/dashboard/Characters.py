from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Characters(db.Model):
    __tablename__ = "characters"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username"))
    class_name = db.Column(db.VARCHAR(20), db.ForeignKey("classes_enum.classes"))
    ign = db.Column(db.VARCHAR(12))
    level = db.Column(db.SMALLINT)
    tracking = db.Column(db.VARCHAR(20), db.ForeignKey("tracking_enum.tracking"))
    is_main = db.Column(db.BOOLEAN, default=False)
    stats = db.Column(db.INT)
    dojo = db.Column(db.SMALLINT)
    ba = db.Column(db.SMALLINT)
    image = db.Column(db.LargeBinary)

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
    stats = fields.Int()
    dojo = fields.Int()
    ba = fields.Int()
    image = fields.Raw()


characters_schema = CharactersSchema()
