from app import db
from flask import request, jsonify, Blueprint
from models.Student import Student, student_schema


users_blueprint = Blueprint("users", __name__)


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
        print(err)

        response = {
            "message": "an error has occured when creating a student"
        }

        return jsonify(response)

