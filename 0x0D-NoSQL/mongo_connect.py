#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
from os import environ

USER_MONGO = environ['USER_MONGO']
PASSWORD = environ['PASSWORD']
DB_MONGO = environ['DB_MONGO']
STRING_CONNECTION = F'mongodb+srv://{USER_MONGO}:{PASSWORD}@cluster0.idafl.mongodb.net/{DB_MONGO}?retryWrites=true&w=majority'


def mongo_client():
    """Create an conection to mongo atlas server."""
    return MongoClient(STRING_CONNECTION)
