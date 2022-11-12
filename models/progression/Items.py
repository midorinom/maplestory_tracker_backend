from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Items(db.Model):
    __tablename__ = "items"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    region = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    slot = db.Column(db.VARCHAR(20), db.ForeignKey("slots_enum.slots"))
    name = db.Column(db.VARCHAR(30))

    def __init__(self, region, slot, name):
        self.region = region
        self.slot = slot
        self.name = name


class ItemsSchema(Schema):
    uuid = fields.UUID()
    region = fields.Str()
    slot = fields.Str()
    name = fields.Str()


items_schema = ItemsSchema()
