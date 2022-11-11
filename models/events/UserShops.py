from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class UserWorldShops(db.Model):
    __tablename__ = "user_world_shops"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username"))
    currency = db.Column(db.VARCHAR(20))
    item = db.Column(db.VARCHAR(30))
    cost = db.Column(db.SMALLINT)
    quantity = db.Column(db.SMALLINT)

    def __init__(self, username, currency, item, cost, quantity):
        self.username = username
        self.currency = currency
        self.item = item
        self.cost = cost
        self.quantity = quantity


class UserWorldShopsSchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    currency = fields.Str()
    item = fields.Str()
    cost = fields.Int()
    quantity = fields.Int()


user_world_shops_schema = UserWorldShopsSchema()


class UserCharacterShops(db.Model):
    __tablename__ = "user_character_shops"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))
    currency = db.Column(db.VARCHAR(20))
    item = db.Column(db.VARCHAR(30))
    cost = db.Column(db.SMALLINT)
    quantity = db.Column(db.SMALLINT)

    def __init__(self, character, currency, item, cost, quantity):
        self.character = character
        self.currency = currency
        self.item = item
        self.cost = cost
        self.quantity = quantity


class UserCharacterShopsSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    currency = fields.Str()
    item = fields.Str()
    cost = fields.Int()
    quantity = fields.Int()


user_character_shops_schema = UserCharacterShopsSchema()
