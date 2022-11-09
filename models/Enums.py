from app import db
from flask import Blueprint
# from marshmallow import Schema, fields


enums_blueprint = Blueprint("enums", __name__)


class Roles_enum(db.Model):
    __tablename__ = "roles_enum"
    roles = db.Column(db.VARCHAR(20), primary_key=True)

    def __init__(self, roles):
        self.roles = roles


# class RolesSchema(Schema):
#     roles = fields.Str()


# role_schema = RolesSchema()
