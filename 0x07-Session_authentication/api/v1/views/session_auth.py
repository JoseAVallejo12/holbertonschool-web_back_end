#!/usr/bin/env python3
""" Module of auth views
"""

from os import getenv
from api.v1.views.index import status
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def Session_authentication() -> str:
    """Session authentication method."""
    if request.form.get('email') is None:
        return jsonify({"error": "email missing"}), 400
    elif request.form.get('password') is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': request.form.get('email')})
    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    elif user[0].is_valid_password(request.form.get('password')):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    out = jsonify(user[0].to_json())
    out.set_cookie(getenv('SESSION_NAME'), user[0].id)
    return out
