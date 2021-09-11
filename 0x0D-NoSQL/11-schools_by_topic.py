#!/usr/bin/env python3
"""Get an list of school having a specific topic."""

def schools_by_topic(mongo_collection, topic):
    """Main function to get list of collection."""
    return mongo_collection.find({'topics': {'$in': [topic]}})
