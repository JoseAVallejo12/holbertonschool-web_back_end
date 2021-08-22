#!/usr/bin/env python3
"""Basic auth class."""
from typing import Union
import bcrypt
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """hash password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate UUID code."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user."""
        user: User
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            newPass = _hash_password(password)
            return self._db.add_user(email, newPass)
        if user:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Valid login."""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('UTF-8'), user.hashed_password):
                return True
        except Exception:
            pass
        return False

    def create_session(self, email: str) -> str:
        """Create session ID if user exist in DB."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            pass

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Return User or None if session id not exist."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Update key session_id in user."""
        if user_id:
            self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> Union[str, None]:
        """Generate reset password token."""
        if email is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update user password."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password=password)
            self._db.update_user(user_id=user.id, hashed_password=hashed_pwd)
            self._db.update_user(user_id=user.id, reset_token=None)

        except Exception:
            raise ValueError
