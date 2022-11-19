from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class UserWorldCurrency(db.Model):
    __tablename__ = "user_world_currency"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username", ondelete="CASCADE"))
    currency = db.Column(db.VARCHAR(20))
    amount = db.Column(db.SMALLINT, default=0)

    def __init__(self, username, currency):
        self.username = username
        self.currency = currency


class UserWorldCurrencySchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    currency = fields.Str()
    amount = fields.Int()


user_world_currency_schema = UserWorldCurrencySchema()


class UserCharacterCurrency(db.Model):
    __tablename__ = "user_character_currency"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid", ondelete="CASCADE"))
    currency = db.Column(db.VARCHAR(20))
    amount = db.Column(db.SMALLINT, default=0)

    def __init__(self, character, currency):
        self.character = character
        self.currency = currency


class UserCharacterCurrencySchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    currency = fields.Str()
    amount = fields.Int()


user_character_currency_schema = UserCharacterCurrencySchema()
