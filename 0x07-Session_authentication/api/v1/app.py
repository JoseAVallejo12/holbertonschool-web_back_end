#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask.globals import g
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from flask_cors import (CORS)
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, jsonify, abort, request
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_db_auth import SessionDBAuth
from api.v1.auth.session_exp_auth import SessionExpAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv('AUTH_TYPE') == 'auth':
    auth = Auth()
elif getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()
elif getenv('AUTH_TYPE') == 'session_auth':
    auth = SessionAuth()
elif getenv('AUTH_TYPE') == 'session_exp_auth':
    auth = SessionExpAuth()
elif getenv('AUTH_TYPE') == 'session_db_auth':
    auth = SessionDBAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not found authorizedX
    """
    return jsonify({"error": error.description}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden resource
    """
    return jsonify({"error": error.description}), 403


@app.before_request
def before_request() -> str:
    """Handle request."""
    exclude_paths = ['/api/v1/status/', '/api/v1/auth_session/login/',
                     '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if not auth or not auth.require_auth(request.path, exclude_paths):
        return None

    if (auth.authorization_header(request) is None
            and auth.session_cookie(request) is None):
        abort(401,  description="Unauthorized")

    if (auth.current_user(request) is None):
        abort(403,  description="Forbidden")
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
