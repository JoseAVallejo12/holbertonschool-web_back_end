#!/usr/bin/env python3
"""changes all topics of a school document based on the name."""

def update_topics(mongo_collection, name, topics):
    """Update collection based in name"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
