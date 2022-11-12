from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class WeeklyMesos(db.Model):
    __tablename__ = "weekly_mesos"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.VARCHAR(20), db.ForeignKey("users.username"))
    first_day_of_bossing_week = db.Column(db.DATE)
    ursus = db.Column(db.BIGINT, default=0)
    tour = db.Column(db.BIGINT, default=0)
    bossing = db.Column(db.BIGINT, default=0)
    farming = db.Column(db.BIGINT, default=0)

    def __init__(self, username, first_day_of_bossing_week):
        self.username = username
        self.first_day_of_bossing_week = first_day_of_bossing_week


class WeeklyMesosSchema(Schema):
    uuid = fields.UUID()
    username = fields.Str()
    first_day_of_bossing_week = fields.Date()
    ursus = fields.Int()
    tour = fields.Int()
    bossing = fields.Int()
    farming = fields.Int()


weekly_mesos_schema = WeeklyMesosSchema()
