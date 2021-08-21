#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_user():
    user_data = request.get_json()
    try:
        user = AUTH.register_user(user_data['email'], user_data['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
