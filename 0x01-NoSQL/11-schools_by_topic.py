#!/usr/bin/env python3
""" specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    """
    return = mongo_collection.find({"topics": topic})
