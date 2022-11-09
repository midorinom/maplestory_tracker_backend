from app import db
from flask import request, jsonify, Blueprint
from models.login.Users import Users, users_schema


users_blueprint = Blueprint("users", __name__)


# Register
@users_blueprint.post("/users/register")
def register():
    json_data = request.get_json()

    try:
        data = users_schema.load(json_data)

        new_user = Users(username=data["username"], password=data["password"], role="NORMAL")
        db.session.add(new_user)
        db.session.commit()

        db_new_user = users_schema.dump(Users.query.get(data["username"]))
        response = {
            "message": "User is created",
            "new_user": db_new_user
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
        data = users_schema.load(json_data)

        new_admin_user = Users(username=data["username"], password=data["password"], role="ADMIN")
        db.session.add(new_admin_user)
        db.session.commit()

        db_new_admin_user = users_schema.dump(Users.query.get(data["username"]))
        response = {
            "message": "Admin user is created",
            "new_admin_user": db_new_admin_user
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
def login():
    json_data = request.get_json()

    try:
        user = users_schema.dump(Users.query.get(json_data["username"]))
        if json_data["password"] == user["password"]:
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

