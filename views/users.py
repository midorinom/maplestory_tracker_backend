from app import db
from flask import request, jsonify, Blueprint
from marshmallow import Schema, fields


users_blueprint = Blueprint("users", __name__)


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


@users_blueprint.post("/submit")
def submit():
    json_data = request.get_json()

    try:
        data = student_schema.load(json_data)

        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]

        student = Student(fname, lname, email)
        db.session.add(student)
        db.session.commit()

        new_student = student_schema.dump(Student.query.get(student.id))
        response = {
            "message": "Student Created",
            "new_student": new_student
        }

        return jsonify(response)

    except Exception as err:
        print(err.messages)

        response = {
            "message": "an error has occured when creating a student"
        }

        return jsonify(response)

