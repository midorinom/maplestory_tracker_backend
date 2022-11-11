from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class EventsWorldShopsGms(db.Model):
    __tablename__ = "events_world_shops_gms"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency = db.Column(db.VARCHAR(20))
    item = db.Column(db.VARCHAR(30))
    cost = db.Column(db.SMALLINT)
    quantity = db.Column(db.SMALLINT)

    def __init__(self, currency, item, cost, quantity):
        self.currency = currency
        self.item = item
        self.cost = cost
        self.quantity = quantity


class EventsWorldShopsGmsSchema(Schema):
    uuid = fields.UUID()
    currency = fields.Str()
    item = fields.Str()
    cost = fields.Int()
    quantity = fields.Int()


events_world_shops_gms_schema = EventsWorldShopsGmsSchema()


class EventsWorldShopsMsea(db.Model):
    __tablename__ = "events_world_shops_msea"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency = db.Column(db.VARCHAR(20))
    item = db.Column(db.VARCHAR(30))
    cost = db.Column(db.SMALLINT)
    quantity = db.Column(db.SMALLINT)

    def __init__(self, currency, item, cost, quantity):
        self.currency = currency
        self.item = item
        self.cost = cost
        self.quantity = quantity


class EventsWorldShopsMseaSchema(Schema):
    uuid = fields.UUID()
    currency = fields.Str()
    item = fields.Str()
    cost = fields.Int()
    quantity = fields.Int()


events_world_shops_msea_schema = EventsWorldShopsMseaSchema()
