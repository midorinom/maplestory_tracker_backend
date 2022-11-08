from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

app = Flask(__name__)


database_uri = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = SQLAlchemy(app)

migrate = Migrate(app, db)
CORS(app)


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


@app.get("/")
def index():
    return "Hello World!"


@app.route("/submit", methods=["POST"])
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
