import pymongo
import sys

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get your db handle
db = connection.test
things = db.things

def using_upsert():
    print 'updating with upsert'

    try:
        # remove any records in the tings collection
        # could use things.remove({}) - but drop moe efficient
        things.drop()

        things.update({'thing':'apple'}, {'$set':{'color':'red', 'taste':'tannic'}}, upsert=True)
        things.update({'thing':'lychee'}, {'$set':{'color':'pink', 'genus':'Soapberry'}}, upsert=True)
        things.update({'thing':'durian'}, {'$set':{'color':'brown', 'smell':'putrid'}, upsert=True})

        durian = things.find_one({'thing':'durian'})
        print 'Behold the durian: ', durian
        lychee = things.find_one({'thing':'lychee'})
        print 'Behold the lychee: ', lychee

    except:
        print 'Shocking error: ', sys.exc_info()[0]
        raise

using_upsert()
        