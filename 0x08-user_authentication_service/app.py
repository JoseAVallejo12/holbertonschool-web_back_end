#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request


app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
