import sys
import pymongo

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get a handle to the school db
db=connection.reddit
stories = db.stories

def find():
    print 'find, at your command'

    query = { 'title': { '$regex': 'Apple' } }
    projection = { 'title': 1, '_id': 0 }

    try:
        curs = stories.find(query,projection)
    except:
        print 'Unknown error: ', sys.exc_info()[0]

    sanity = 0
    for doc in curs:
        print doc
        sanity += 1
        if sanity > 10:
            break

find()