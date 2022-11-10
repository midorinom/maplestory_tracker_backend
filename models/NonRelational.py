from app import db
from flask import Blueprint
from marshmallow import Schema, fields


non_relational_blueprint = Blueprint("non-relational", __name__)


# Dailies Default
class DailiesDefault(db.Model):
    __tablename__ = "dailies_default"
    dailies_list = db.Column(db.VARCHAR(50), primary_key=True)

    def __init__(self, dailies_list):
        self.dailies_list = dailies_list


class DailiesDefaultSchema(Schema):
    dailies_list = fields.Str()


dailies_default_schema = DailiesDefaultSchema()


# Weeklies Default
class WeekliesDefault(db.Model):
    __tablename__ = "weeklies_default"
    weeklies_list = db.Column(db.VARCHAR(50), primary_key=True)

    def __init__(self, weeklies_list):
        self.weeklies_list = weeklies_list


class WeekliesDefaultSchema(Schema):
    weeklies_list = fields.Str()


weeklies_defualt_schema = WeekliesDefaultSchema()


# BossesGms
class BossesGms(db.Model):
    __tablename__ = "bosses_gms"
    id = db.Column(db.SMALLINT, primary_key=True)
    name = db.Column(db.VARCHAR(20))
    crystal = db.Column(db.BIGINT)

    def __init__(self, name, crystal):
        self.name = name
        self.crystal = crystal


class BossesGmsSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    crystal = fields.Int()


bosses_gms_schema = BossesGmsSchema()


# BossesMsea
class BossesMsea(db.Model):
    __tablename__ = "bosses_msea"
    id = db.Column(db.SMALLINT, primary_key=True)
    name = db.Column(db.VARCHAR(20))
    crystal = db.Column(db.BIGINT)

    def __init__(self, name, crystal):
        self.name = name
        self.crystal = crystal


class BossesMseaSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    crystal = fields.Int()


bosses_msea_schema = BossesMseaSchema()
