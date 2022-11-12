from app import db
from flask import request, jsonify, Blueprint
from models.progression.Items import Items, items_schema


progression_admin_blueprint = Blueprint("progression_admin", __name__)


# Add Item
@progression_admin_blueprint.put("/progression-admin/items/add")
def add_item():
    json_data = request.get_json()

    try:
        data = items_schema.load(json_data)

        new_item = Items(region=data["region"], slot=data["slot"], name=data["name"])
        db.session.add(new_item)
        db.session.commit()

        response = {
             "message": "Item is added",
         }
        return jsonify(response), 201

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when adding item"
        }
        return jsonify(response), 400


# Update Item
@progression_admin_blueprint.patch("/progression-admin/items/update")
def update_item():
    json_data = request.get_json()

    try:
        data = items_schema.load(json_data)

        Items.query.filter(Items.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Item is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating item"
        }
        return jsonify(response), 400


# Delete Item
@progression_admin_blueprint.delete("/progression-admin/items/delete")
def delete_legion():
    json_data = request.get_json()

    try:
        data = items_schema.load(json_data)

        Items.query.filter(Items.uuid == data["uuid"]).delete()
        db.session.commit()

        response = {
            "message": "Item is deleted",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when deleting the item"
        }
        return jsonify(response), 400
