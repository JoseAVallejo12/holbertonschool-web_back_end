#!/usr/bin/env python3
"""Auth class for the app."""

from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64
import uuid


class BasicAuth(Auth):
    """Basic Auth class."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract_base64_authorization_header."""
        if (self.__isInValid(authorization_header)
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header.split(' ')[1].lstrip()

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decode_base64_authorization_header."""
        if self.__isInValid(base64_authorization_header):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """Extract_user_credentials."""
        if (self.__isInValid(decoded_base64_authorization_header)
                or decoded_base64_authorization_header.count(':') == 0):
            return (None, None)
        headers = decoded_base64_authorization_header.split(':')
        return (headers[0].lstrip(), headers[1].lstrip())

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """User_object_from_credentials."""
        if self.__isInValid(user_email) or self.__isInValid(user_pwd):
            return None

        user = User()
        user.load_from_file()
        users = user.search({'email': user_email})
        if (len(users) == 0) or not users[0].is_valid_password(user_pwd):
            return None

        return users[0]

    def __isInValid(self, parametter: str) -> bool:
        """Validate arg commin to function"""
        if (parametter is None or not isinstance(parametter, str)):
            return True
        return False


""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()

""" Retreive this user via the class BasicAuth """
a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials("email@notfound.com", "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else "None")
