import pymongo
import sys

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get a handle to the school db
db=connection.test
scores = db.scores

def find():
    print 'find, reporting for duty'

    query = { 'type': 'exam' }
    selector ={ 'student': 1, '_id': 0 }

    try:
        curs = scores.find(query).sort('student', pymongo.ASCENDING).skip(4).limit(1)
    except:
        print 'Unexpected error: ', sys.exc_info()[0]


    for doc in curs:
        print doc

