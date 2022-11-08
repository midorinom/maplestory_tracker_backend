from app import db
from marshmallow import Schema, fields


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    email = db.Column(db.String(40))

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email


class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    fname = fields.Str()
    lname = fields.Str()
    email = fields.Str()


student_schema = StudentSchema()
