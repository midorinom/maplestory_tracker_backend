from flask import request, jsonify, Blueprint
from app import db


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


@users_blueprint.post("/submit")
def submit():
    data = request.get_json()
    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]

    student = Student(fname, lname, email)
    db.session.add(student)
    db.session.commit()

    response = {
        "message": "Student Created"
    }
    return jsonify(response)
