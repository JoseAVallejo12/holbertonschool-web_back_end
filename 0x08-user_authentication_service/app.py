#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from flask.wrappers import Response
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_user() -> Response:
    """Register an new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> Response:
    """Login method."""
    email = request.form.get('email')
    password = request.form.get('password')
    if not(email) or not(password):
        abort(401)
    if not(AUTH.valid_login(email=email, password=password)):
        abort(401)
    res = make_response({"email": email, "message": "logged in"})
    res.set_cookie('session_id', AUTH.create_session(email))
    return res


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> Response:
    """Method loggin exit."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user_id=user.id)
    return redirect("/")


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> Response:
    """Method loggin exit."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({'email': user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
