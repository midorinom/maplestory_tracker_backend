from app import db
from flask import Blueprint


models_enums_blueprint = Blueprint("models_enums", __name__)


# Roles
class Roles(db.Model):
    __tablename__ = "roles_enum"
    roles = db.Column(db.VARCHAR(20), primary_key=True)


# Classes
class Classes(db.Model):
    __tablename__ = "classes_enum"
    classes = db.Column(db.VARCHAR(20), primary_key=True)
    region = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))


# Slots
class Slots(db.Model):
    __tablename__ = "slots_enum"
    slots = db.Column(db.VARCHAR(20), primary_key=True)
