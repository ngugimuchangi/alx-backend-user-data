#!/usr/bin/env python3
"""
Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
app.url_map.strict_slashes = False
auth = Auth()


@app.route("/")
def home() -> str:
    """ Home endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> tuple[str, int]:
    """ Register's new user
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already register"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
