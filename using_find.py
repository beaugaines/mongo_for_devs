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

    query = {'type':'exam'}
    selector ={'student': 1, '_id':0}

    try:
        curs = scores.find(query, selector)
    except:
        print 'Unexpected error: ', sys.exc_info()[0]

    sanity = 0
    for doc in curs:
        print doc
        sanity += 1
        if (sanity > 10):
            break


def find_one():

    print 'find one, at your service'

    query = {'student':10}

    try:
        doc = scores.find_one(query)
    except:
        print 'Unexpected error: ', sys.exc_info()[0]

    print doc

find()