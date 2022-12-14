from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class Farming(db.Model):
    __tablename__ = "farming"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid", ondelete="CASCADE"))
    date = db.Column(db.DATE)
    first_day_of_week = db.Column(db.DATE)
    first_day_of_bossing_week = db.Column(db.DATE)
    is_current_week = db.Column(db.BOOLEAN, default=True)
    hours = db.Column(db.SMALLINT)
    minutes = db.Column(db.SMALLINT)
    mesos = db.Column(db.BIGINT, default=0)

    def __init__(self, character, date, first_day_of_week, first_day_of_bossing_week):
        self.character = character
        self.date = date
        self.first_day_of_week = first_day_of_week
        self.first_day_of_bossing_week = first_day_of_bossing_week


class FarmingSchema(Schema):
    uuid = fields.UUID()
    character = fields.UUID()
    date = fields.Date()
    first_day_of_week = fields.Date()
    first_day_of_bossing_week = fields.Date()
    is_current_week = fields.Bool()
    hours = fields.Int()
    minutes = fields.Int()
    mesos = fields.Int()


farming_schema = FarmingSchema()
