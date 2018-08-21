import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://172.19.0.8:27017")
db = client.test_database

collection = db.test_collection
collection = db["documents"]
result = collection.find()
print("esco")
for obj in collection.find():
    print("entro")
    print(obj)
print(result)

# collection = db.test_collection
# posts = db.posts
# pprint.pprint(posts.find_one())
# print(db.collection_names(include_system_collections=False))
# for post in posts.find():
#     pprint.pprint(post)
# print(posts.count())

#db = client.test_database
#db = client['...']
#collection = db.test_collection
#collection = db["..."]
#result = collection.find()
#obj = next(result, None)
#if obj:
#  username= obj['username']
#  print username