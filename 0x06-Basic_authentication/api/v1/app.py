#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Not found authorized
    """
    return jsonify({"error": error.description}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden resource
    """
    return jsonify({"error": error.description}), 403


@app.before_request
def before_request():
    exclude_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if isinstance(auth, Auth):
        if not auth.require_auth(request.path, exclude_paths):
            return

        if (auth.authorization_header(request) is None):
            abort(401,  description="Unauthorized")

        if (auth.current_user(request) is None):
            abort(403,  description="Forbidden")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    if getenv('AUTH_TYPE') == 'auth':
        from api.v1.auth.auth import Auth
        auth = Auth()
    app.run(host=host, port=port, debug=True)
