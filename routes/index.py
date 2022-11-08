from flask import Blueprint


index_blueprint = Blueprint("index", __name__)


@index_blueprint.get("/")
def index():
    return "Hello World!"


@index_blueprint.get("/test")
def test():
    return "Hello test!"