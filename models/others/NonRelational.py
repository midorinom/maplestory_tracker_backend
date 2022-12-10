from app import db
from flask import Blueprint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from marshmallow import Schema, fields


non_relational_blueprint = Blueprint("non-relational", __name__)


# Dailies Default
class DailiesDefault(db.Model):
    __tablename__ = "dailies_default"
    dailies_list = db.Column(db.VARCHAR(50), primary_key=True)


# Weeklies Default
class WeekliesDefault(db.Model):
    __tablename__ = "weeklies_default"
    weeklies_list = db.Column(db.VARCHAR(50), primary_key=True)


# Bosses
class Bosses(db.Model):
    __tablename__ = "bosses"
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = db.Column(db.SMALLINT)
    region = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    name = db.Column(db.VARCHAR(20))
    crystal = db.Column(db.BIGINT)


class BossesSchema(Schema):
    id = fields.Int()
    region = fields.Str()
    name = fields.Str()
    crystal = fields.Int()


bosses_schema = BossesSchema()
