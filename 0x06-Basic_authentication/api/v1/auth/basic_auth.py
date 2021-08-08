#!/usr/bin/env python3
"""Auth class for the app."""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract_base64_authorization_header."""
        if (authorization_header is None
            or not isinstance(authorization_header, str)
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header.split(' ')[1].lstrip()
