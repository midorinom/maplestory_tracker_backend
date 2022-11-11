from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class EventsSubGms(db.Model):
    __tablename__ = "events_sub_gms"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(30))
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class EventsSubGmsSchema(Schema):
    uuid = fields.UUID()
    name = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


events_sub_gms_schema = EventsSubGmsSchema()


class EventsSubMsea(db.Model):
    __tablename__ = "events_sub_msea"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(30))
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class EventsSubMseaSchema(Schema):
    uuid = fields.UUID()
    name = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


events_sub_msea_schema = EventsSubMseaSchema()
