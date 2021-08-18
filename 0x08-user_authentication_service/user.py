#!/usr/bin/env python3
"""SQLAlchemy maping class user."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false

Base = declarative_base()


class User(Base):
    """Main class mapping user."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=false)
    hashed_password = Column(String(250), nullable=false)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
