from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class UrsusTour(db.Model):
    __tablename__ = "ursus_tour"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username", ondelete="CASCADE"))
    date = db.Column(db.DATE)
    first_day_of_bossing_week = db.Column(db.DATE)
    ursus = db.Column(db.INT, default=0)
    tour = db.Column(db.INT, default=0)

    def __init__(self, username, date, first_day_of_bossing_week):
        self.username = username
        self.date = date
        self.first_day_of_bossing_week = first_day_of_bossing_week


class UrsusTourSchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    date = fields.Date()
    first_day_of_bossing_week = fields.Date()
    ursus = fields.Int()
    tour = fields.Int()


ursus_tour_schema = UrsusTourSchema()
