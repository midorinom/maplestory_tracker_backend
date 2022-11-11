from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


class EventsMain(db.Model):
    __tablename__ = "events_main"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    region = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    name = db.Column(db.VARCHAR(30))
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)


class EventsMainSchema(Schema):
    uuid = fields.UUID()
    region = fields.Str()
    name = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()


events_main_schema = EventsMainSchema()
