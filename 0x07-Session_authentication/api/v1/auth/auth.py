#!/usr/bin/env python3
"""Auth class for the app."""

from typing import List, TypeVar
from flask import request
from os import getenv


class Auth:
    """Auth main class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Protect path."""
        if excluded_paths is None:
            return True
        for element in excluded_paths:
            if "*" in element:
                return not(path.startswith(element.replace("*", "")))
        return not(path in excluded_paths or f'{path}/' in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Authorization header."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user function."""
        return None

    def session_cookie(self, request=None):
        """Session cookie."""
        if request is None:
            return None
        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
