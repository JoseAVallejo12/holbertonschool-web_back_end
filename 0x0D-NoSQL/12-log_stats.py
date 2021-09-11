#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient

def view_logs(mongo_collection):
    """main method for ins"""
    count = mongo_collection.find().count()
    get_count = mongo_collection.find({"method": {"$in": ["GET"]}}).count()
    post_count = mongo_collection.find({"method": {"$in": ["POST"]}}).count()
    put_count = mongo_collection.find({"method": {"$in": ["PUT"]}}).count()
    patch_count = mongo_collection.find({"method": {"$in": ["PATCH"]}}).count()
    delete_count = mongo_collection.find({"method": {"$in": ["DELETE"]}}).count()
    print(f'{count} logs')
    print('Methods:')
    print(f'\tmethod GET: {get_count}')
    print(f'\tmethod POST: {post_count}')
    print(f'\tmethod PUT: {put_count}')
    print(f'\tmethod PATCH: {patch_count}')
    print(f'\tmethod DELETE: {delete_count}')

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    view_logs(nginx_collection)
