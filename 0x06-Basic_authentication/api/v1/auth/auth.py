#!/usr/bin/env python3
"""Auth class for the app."""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth main class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Protect path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user function."""
        return None
