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
from models.Enums import models_enums_blueprint
from models.NonRelational import non_relational_blueprint

app.register_blueprint(models_enums_blueprint)
app.register_blueprint(non_relational_blueprint)

# Register views blueprints
from views.enums import views_enums_blueprint
from views.users import users_blueprint
from views.characters import characters_blueprint
from views.dailies import dailies_blueprint
from views.weeklies import weeklies_blueprint
from views.ursusTour import ursus_tour_blueprint
from views.bossing import bossing_blueprint
from views.legion import legion_blueprint

app.register_blueprint(views_enums_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(characters_blueprint)
app.register_blueprint(dailies_blueprint)
app.register_blueprint(weeklies_blueprint)
app.register_blueprint(ursus_tour_blueprint)
app.register_blueprint(bossing_blueprint)
app.register_blueprint(legion_blueprint)
