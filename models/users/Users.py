from app import db
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.VARCHAR(20), primary_key=True)
    role = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    pw_hash = db.Column(db.VARCHAR(60))
    event = db.Column(db.VARCHAR(30))

    def __init__(self, username, role, pw_hash):
        self.username = username
        self.role = role
        self.pw_hash = pw_hash


class UsersSchema(Schema):
    username = fields.Str()
    role = fields.Str()
    pw_hash = fields.Str()
    event = fields.Str()


users_schema = UsersSchema()
