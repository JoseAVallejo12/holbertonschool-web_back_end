#!/usr/bin/env python3
"""Auth class for the app."""

from typing import Tuple
from api.v1.auth.auth import Auth
import base64


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

    def __isInValid(self, parametter: str) -> bool:
        """Validate arg commin to function"""
        if (parametter is None or not isinstance(parametter, str)):
            return True
        return False
