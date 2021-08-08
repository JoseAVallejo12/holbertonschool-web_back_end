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

        return authorization_header.removeprefix("Basic").lstrip()


a = BasicAuth()

print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header("Holberton School"))
print(a.extract_base64_authorization_header("Basic Holberton"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(a.extract_base64_authorization_header("Basic1234"))
