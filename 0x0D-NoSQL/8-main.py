#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
mongo_client = __import__('mongo_connect').mongo_client

if __name__ == "__main__":
    client = mongo_client()
    school_collection = client.Holberton.school
    schools = list_all(school_collection)
    print(school_collection.find_one())
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
