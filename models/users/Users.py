from app import db
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.VARCHAR(20), primary_key=True)
    role = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    pw_hash = db.Column(db.VARCHAR(60))
    main = db.Column(UUID(as_uuid=True), db.ForeignKey("characters.uuid"))

    def __init__(self, username, role, pw_hash):
        self.username = username
        self.role = role
        self.pw_hash = pw_hash


class UsersSchema(Schema):
    username = fields.Str()
    role = fields.Str()
    pw_hash = fields.Str()
    main = fields.UUID()


users_schema = UsersSchema()
