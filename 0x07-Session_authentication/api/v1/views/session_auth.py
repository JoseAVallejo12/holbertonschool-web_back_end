#!/usr/bin/env python3
""" Module of auth views
"""

from os import getenv
from api.v1.views.index import status
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login/', methods=['POST'],
                 strict_slashes=False)
def Session_authentication() -> str:
    """Session authentication method."""
    if request.form.get('email') is None:
        return jsonify({"error": "email missing"}), 400
    elif request.form.get('password') is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': request.form.get('email')})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(request.form.get('password')):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user_found = users[0]
    session_id = auth.create_session(user_found.id)
    response = jsonify(user_found.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ DELETE /auth_session/logout
    Return:
     - Empty json
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
