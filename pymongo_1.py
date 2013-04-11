import pymongo

from pymongo import MongoClient

# connect to db
connection = MongoClient('localhost', 27017)

# connect to the test db
db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']



