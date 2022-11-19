from app import db
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.VARCHAR(20), primary_key=True)
    role = db.Column(db.VARCHAR(20), db.ForeignKey("roles_enum.roles"))
    pw_hash = db.Column(db.VARCHAR(60))
    event = db.Column(db.VARCHAR(30))

    # Relationships
    ursus_tour = relationship("UrsusTour", backref="users", passive_deletes=True)
    weekly_mesos = relationship("WeeklyMesos", backref="users", passive_deletes=True)
    user_world_currency = relationship("UserWorldCurrency", backref="users", passive_deletes=True)
    user_world_shops = relationship("UserWorldShops", backref="users", passive_deletes=True)
    legion = relationship("Legion", backref="users", passive_deletes=True)

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
