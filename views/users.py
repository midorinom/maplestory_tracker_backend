from app import app, db
from flask import request, jsonify, Blueprint
from models.login.Users import Users, users_schema
from flask_bcrypt import Bcrypt


users_blueprint = Blueprint("users", __name__)
bcrypt = Bcrypt(app)


# Register
@users_blueprint.post("/users/register")
def register():
    json_data = request.get_json()

    try:
        pw_hash = bcrypt.generate_password_hash(json_data["password"], 15).decode("utf-8")

        data = users_schema.load({
            "username": json_data["username"],
            "pw_hash": pw_hash
        })

        new_user = Users(username=data["username"], pw_hash=pw_hash, role="NORMAL")
        db.session.add(new_user)
        db.session.commit()

        db_new_user = users_schema.dump(Users.query.get(data["username"]))
        response = {
             "message": "User is created",
             "new_user": db_new_user["username"]
         }

        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when creating a new user"
        }

        return jsonify(response), 400


# Register Admin
@users_blueprint.post("/users/register-admin")
def register_admin():
    json_data = request.get_json()

    try:
        pw_hash = bcrypt.generate_password_hash(json_data["password"], 15).decode("utf-8")

        data = users_schema.load({
            "username": json_data["username"],
            "pw_hash": pw_hash
        })

        new_admin_user = Users(username=data["username"], pw_hash=pw_hash, role="ADMIN")
        db.session.add(new_admin_user)
        db.session.commit()

        db_new_admin_user = users_schema.dump(Users.query.get(data["username"]))
        response = {
            "message": "Admin user is created",
            "new_admin_user": db_new_admin_user["username"]
        }

        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when creating a new admin user"
        }

        return jsonify(response), 400


# Login
@users_blueprint.post("/users/login")
async def login():
    json_data = request.get_json()

    try:
        user = users_schema.dump(Users.query.get(json_data["username"]))

        if bcrypt.check_password_hash(user["pw_hash"], json_data["password"]):
            response = {
                "message": "Login is successful",
                "role": user["role"]
            }
            return jsonify(response), 200
        else:
            response = {
                "message": "Unauthorised, login failed",
            }
            return jsonify(response), 401

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when logging in"
        }

        return jsonify(response), 400

