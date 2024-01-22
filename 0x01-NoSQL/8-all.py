#!/usr/bin/env python3
""" List all documents in Python """

def list_all(mongo_collection):
    """ Python function that lists all documents in a collection """
    documents = mongo_collection.find()

    if documents:
        return [document for document in documents]
    return []
