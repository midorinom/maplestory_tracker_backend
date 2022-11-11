from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class EventsMainGms(db.Model):
    __tablename__ = "events_main_gms"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(30))
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class EventsMainGmsSchema(Schema):
    uuid = fields.UUID()
    name = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


events_main_gms_schema = EventsMainGmsSchema()


class EventsMainMsea(db.Model):
    __tablename__ = "events_main_msea"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(30))
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class EventsMainMseaSchema(Schema):
    uuid = fields.UUID()
    name = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


events_main_msea_schema = EventsMainMseaSchema()
