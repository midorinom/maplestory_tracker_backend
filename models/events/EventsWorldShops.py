from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class EventsWorldShops(db.Model):
    __tablename__ = "events_world_shops"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    region = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    currency = db.Column(db.VARCHAR(20))
    item = db.Column(db.VARCHAR(30))
    cost = db.Column(db.SMALLINT)
    quantity = db.Column(db.SMALLINT)

    def __init__(self, region, currency, item, cost, quantity):
        self. region = region
        self.currency = currency
        self.item = item
        self.cost = cost
        self.quantity = quantity


class EventsWorldShopsSchema(Schema):
    uuid = fields.UUID()
    region = fields.Str()
    currency = fields.Str()
    item = fields.Str()
    cost = fields.Int()
    quantity = fields.Int()


events_world_shops_schema = EventsWorldShopsSchema()
