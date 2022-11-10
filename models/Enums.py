from app import db
from flask import Blueprint


enums_blueprint = Blueprint("enums", __name__)


# Roles
class Roles(db.Model):
    __tablename__ = "roles_enum"
    roles = db.Column(db.VARCHAR(20), primary_key=True)

    def __init__(self, roles):
        self.roles = roles


# Classes
class Classes(db.Model):
    __tablename__ = "classes_enum"
    classes = db.Column(db.VARCHAR(20), primary_key=True)

    def __init__(self, classes):
        self.classes = classes
