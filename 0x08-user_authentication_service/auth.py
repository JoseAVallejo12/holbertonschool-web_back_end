#!/usr/bin/env python3
"""Basic auth class."""
import bcrypt
from sqlalchemy.sql.expression import false
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hash password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


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
