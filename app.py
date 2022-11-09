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


# Register blueprints
from models.Enums import enums_blueprint
from views.users import users_blueprint

app.register_blueprint(enums_blueprint)
app.register_blueprint(users_blueprint)