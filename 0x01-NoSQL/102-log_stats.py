#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_col = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(nginx_col.count_documents({})))
    print("Methods:")

    for method in methods:
        print("\tmethod {}: {}".format(
            method, nginx_col.count_documents({"method": method})))

    print("{} status check".format(
        nginx_col.count_documents({"method": "GET", "path": "/status"})))

    ips = nginx_col.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for s in ips:
        print(f"\t{s.get('_id')}: {s.get('count')}")
