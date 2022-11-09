from app import db
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.VARCHAR(20), primary_key=True)
    role = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    password = db.Column(db.VARCHAR(60))

    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password


class UsersSchema(Schema):
    username = fields.Str()
    role = fields.Str()
    password = fields.Str()


users_schema = UsersSchema()
