#!/usr/bin/env python3
""" Insert a document in Python """

def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    Returns the new _id
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
