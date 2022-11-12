from app import db
from flask import request, jsonify, Blueprint
from models.bossing.Bossing import Bossing, bossing_schema
import datetime
from models.others.NonRelational import Bosses, bosses_schema


bossing_blueprint = Blueprint("bossing", __name__)


# Get Bossing
@bossing_blueprint.post("/bossing/get")
def get_bossing():
    json_data = request.get_json()

    try:
        # Using today's date, get the first_day_of_bossing_week
        date_list = json_data["date"].split("-")
        date_list = [int(i) for i in date_list]
        date = datetime.date(*date_list)

        # timedelta subtracts the current weekday (converted to a value) from today's date, to get Monday's date
        # Then add 3 to get Thursday, which is the day when the bossing week resets
        # The operation involving timedelta returns a datetime Object. strftime formats it back to a string
        first_day_of_bossing_week = (date + datetime.timedelta(days=-date.weekday()+3)).strftime("%Y-%m-%d")

        # Remove date from json_data, add first_day_of_bossing_week
        json_data.pop("date")
        json_data["first_day_of_bossing_week"] = first_day_of_bossing_week

        # Store level and role in a variable, then remove them from json_data, then load json_data
        level = json_data["level"]
        role = json_data["role"]

        json_data.pop("level")
        json_data.pop("role")

        data = bossing_schema.load(json_data)

        # Response dictionary
        response = {
            "message": "Got bossing",
        }

        # Check if there is an existing entry for this week. If so, add it to the response
        bossing = bossing_schema.dump(Bossing.query.filter(
            Bossing.character == data["character"], Bossing.first_day_of_bossing_week == first_day_of_bossing_week))

        if len(bossing) > 0:
            response["bossing"] = bossing[0]
        else:
            # Look up the existing entries
            existing_bossing = bossing_schema.dump(Bossing.query.filter(Bossing.character == data["character"]))

            # Index will be 0 if there is only 1 existing entry
            index = 0

            if len(existing_bossing) == 2:
                # There are 2 existing entries. Check which one is the latest
                date1_list = existing_bossing[0]["first_day_of_bossing_week"].split("-")
                date1_list = [int(i) for i in date1_list]
                date1 = datetime.date(*date1_list)

                date2_list = existing_bossing[1]["first_day_of_bossing_week"].split("-")
                date2_list = [int(i) for i in date2_list]
                date2 = datetime.date(*date2_list)

                # If the second element is the latest entry, set index to 1
                if date2 > date1:
                    index = 1

                # Delete the older entry
                Bossing.query.filter(Bossing.uuid == existing_bossing[0 if index == 1 else 1]["uuid"]).delete()
                db.session.commit()

            # If there are existing entries, set the latest entry to is_current_week=False. Also, set bossing_list
            if len(existing_bossing) > 0:
                Bossing.query.filter(
                    Bossing.uuid == existing_bossing[index]["uuid"]).update({"is_current_week": False})
                db.session.commit()

                bossing_list = existing_bossing[index]["bossing_list"]
            else:
                # Set a hardest_boss value based on the character's level
                if level < 235:
                    # Up to Chaos Vellum
                    hardest_boss = 2
                else:
                    # Up to Normal Damien
                    hardest_boss = 3

                # Using role to filter the region, query from the bosses table and construct a bossing_list
                    bosses = Bosses.query.filter(
                        Bosses.region == role, Bosses.id <= hardest_boss).with_entities(Bosses.name)
                    bosses = [element.name for element in bosses]
                    bossing_list = "@".join(bosses)

            # Make an entry for this week
            new_bossing = Bossing(character=data["character"], first_day_of_bossing_week=first_day_of_bossing_week,
                                  bossing_list=bossing_list)
            db.session.add(new_bossing)
            db.session.commit()
            response["bossing"] = bossing_schema.dump(new_bossing)

        # Return response
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting bossing"
        }
        return jsonify(response), 400


# Update Bossing
@bossing_blueprint.patch("/bossing/update")
def update_bossing():
    json_data = request.get_json()

    try:
        # Using role to filter the region, query from the bosses table and construct a bossing_list
        bosses = Bosses.query.filter(
            Bosses.region == json_data["role"], Bosses.id <= json_data["hardest_boss"]).with_entities(Bosses.name)
        bosses = [element.name for element in bosses]
        bossing_list = "@".join(bosses)

        # Remove role and hardest_boss from json_data, add bossing_list, then load json_data
        json_data.pop("role")
        json_data.pop("hardest_boss")
        json_data["bossing_list"] = bossing_list

        data = bossing_schema.load(json_data)

        # Perform the update
        Bossing.query.filter(Bossing.uuid == data["uuid"]).update(
            {
                **data
            }
        )
        db.session.commit()

        response = {
            "message": "Bossing is updated",
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when updating bossing"
        }
        return jsonify(response), 400


# Get Boss Names and Crystal Prices
@bossing_blueprint.post("/bosses/get")
def get_bosses_name_crystal():
    json_data = request.get_json()

    try:
        bosses = bosses_schema.dump(Bosses.query.filter(
            Bosses.region == json_data["role"]).with_entities(Bosses.name, Bosses.crystal), many=True)

        response = {
            "message": "Got bosses",
            "bosses": bosses
        }
        return jsonify(response), 200

    except Exception as err:
        print(err)

        response = {
            "message": "an error has occured when getting bosses"
        }
        return jsonify(response), 400
