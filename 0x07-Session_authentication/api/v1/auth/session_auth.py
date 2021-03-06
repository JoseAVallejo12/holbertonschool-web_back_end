#!/usr/bin/env python3
"""SessionAuth class for the app."""

import uuid
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth main class."""
    user_id_by_session_id = {}

    def __isInValid(self, parametter: str) -> bool:
        """Validate input arg to function"""
        if (parametter is None or not isinstance(parametter, str)):
            return True
        return False

    def create_session(self, user_id: str = None) -> str:
        """Create an user id."""
        if self.__isInValid(user_id):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({
            session_id: user_id
        })
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """User id for session id."""
        if self.__isInValid(session_id):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user function.(overload)"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        print(self.user_id_by_session_id)
        print(session_id)
        return User.get(self.user_id_for_session_id(session_id))

    def destroy_session(self, request=None):
        """Delete the user session / log out."""
        if request:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            if not self.user_id_for_session_id(session_id):
                return False
            self.user_id_by_session_id.pop(session_id)
            return True
