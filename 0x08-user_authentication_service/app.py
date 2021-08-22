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
    """Profile session id user."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({'email': user.email})
    abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> Response:
    """Return token for Reset password."""
    email = request.form.get('email')
    if email is None:
        abort(403)
    try:
        new_token = AUTH.get_reset_password_token(email=email)
        return jsonify({"email": email, "reset_token": new_token})

    except Exception:
        abort(403)


@app.route("/reset_password", methods=['PUT'])
def update_password() -> Response:
    """Reset password token."""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
