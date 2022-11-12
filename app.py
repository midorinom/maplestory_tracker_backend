from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Configs and declaring variables
load_dotenv()

app = Flask(__name__)
CORS(app)

database_uri = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = SQLAlchemy(app)

migrate = Migrate(app, db)


# Register models blueprints
from models.others.Enums import models_enums_blueprint
from models.others.NonRelational import non_relational_blueprint

app.register_blueprint(models_enums_blueprint)
app.register_blueprint(non_relational_blueprint)

# Register views blueprints
from views.others.enums import views_enums_blueprint
from views.users.users import users_blueprint
from views.characters.characters import characters_blueprint
from views.dailies.dailies import dailies_blueprint
from views.dailies.weeklies import weeklies_blueprint
from views.dailies.ursusTour import ursus_tour_blueprint
from views.bossing.bossing import bossing_blueprint
from views.legion.legion import legion_blueprint
from views.events.eventsAdmin import events_admin_blueprint
from views.events.events import events_blueprint
from views.farming.farming import farming_blueprint
from views.dashboard.weekly_mesos import weekly_mesos_blueprint
from views.progression.progression import progression_blueprint

app.register_blueprint(views_enums_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(characters_blueprint)
app.register_blueprint(dailies_blueprint)
app.register_blueprint(weeklies_blueprint)
app.register_blueprint(ursus_tour_blueprint)
app.register_blueprint(bossing_blueprint)
app.register_blueprint(legion_blueprint)
app.register_blueprint(events_admin_blueprint)
app.register_blueprint(events_blueprint)
app.register_blueprint(farming_blueprint)
app.register_blueprint(weekly_mesos_blueprint)
app.register_blueprint(progression_blueprint)
