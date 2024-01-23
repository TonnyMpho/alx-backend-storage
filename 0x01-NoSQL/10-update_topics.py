#!/usr/bin/env python3
""" Change school topics """

def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of a school document based on the name
    mongo_collection - pymongo collection object
    name (string) the school name to update
    topics (list of strings) list of topics approached in the school
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
