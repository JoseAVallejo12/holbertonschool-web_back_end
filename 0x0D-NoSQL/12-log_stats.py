#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient

def view_logs(mongo_collection):
    """main method for inspetion log"""
    count = mongo_collection.find().count_documents()
    get_count = mongo_collection.find({"method": {"$in": ["GET"]}}).count_documents()
    post_count = mongo_collection.find({"method": {"$in": ["POST"]}}).count_documents()
    put_count = mongo_collection.find({"method": {"$in": ["PUT"]}}).count_documents()
    patch_count = mongo_collection.find({"method": {"$in": ["PATCH"]}}).count_documents()
    delete_count = mongo_collection.find({"method": {"$in": ["DELETE"]}}).count_documents()
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
