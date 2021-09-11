#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
from os import environ
list_all = __import__('8-all').list_all

USER_MONGO = environ['USER_MONGO']
PASSWORD = environ['PASSWORD']
DB_MONGO = environ['DB_MONGO']
STRING_CONNECTION = F'mongodb+srv://{USER_MONGO}:{PASSWORD}@cluster0.idafl.mongodb.net/{DB_MONGO}?retryWrites=true&w=majority'

if __name__ == "__main__":
    client = MongoClient(STRING_CONNECTION)
    school_collection = client.Holberton.school
    schools = list_all(school_collection)
    print(school_collection.find_one())
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
