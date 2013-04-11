import pymongo
import sys

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get a handle to the school db
db=connection.school
scores = db.scores

def find():
    print 'find, reporting for duty'

    query = {'type':'exam'}

