import pymongo

from pymongo import MongoClient

# connect to db
connection = MongoClient('localhost', 27017)

# connect to the test db
db = connection.test

# handle to names collection
scores = db.scores

item = scores.find_one()

print (str(item['type']) + ', ' + str(item['score']))



