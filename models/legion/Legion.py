from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Legion(db.Model):
    __tablename__ = "legion"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username"))
    class_name = db.Column(db.VARCHAR(20), db.ForeignKey("classes_enum.classes"))
    level = db.Column(db.SMALLINT)

    def __init__(self, username, class_name, level):
        self.username = username
        self.class_name = class_name
        self.level = level


class LegionSchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    class_name = fields.Str()
    level = fields.Int()


legion_schema = LegionSchema()
