from flask import Blueprint, jsonify, request


blueprint = Blueprint("users", __name__)


@blueprint.route("/")
def index():
    return jsonify({"msg": "You are not logged in"})


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == "admin" and password == "secret_password":
        return jsonify({"msg": "Logged successfully"})
    return jsonify({"msg": "Bad username or password"}), 401
