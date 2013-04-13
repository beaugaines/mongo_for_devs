import pymongo
import sys

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get your db handle
db = connection.grades
scores = db.scores

# 
