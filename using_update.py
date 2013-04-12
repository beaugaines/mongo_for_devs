import pymongo
import sys
import datetime

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get handle to student db
db=connection.test
scores=db.scores

def remove_review_date():

    db=connection.test
    scores=db.scores
    print '\n\nremoving all review dates'

    try:
        scores.update({}, {'$unset':{'review_date':1}}, multi=True)
    except:
        print 'Unexpected error: ', sys.exc_info()[0]
        raise

# replaces document wholesale
def using_save():

    db=connection.test
    scores=db.scores
    print 'updating record using save'

    try:
        # get the doc
        score = scores.find_one({'student': 1, 'type': 'exam'})
        print 'before: ', score

        # add review date
        score['review_date'] = datetime.datetime.utcnow()

        # update the record with convenience method
        scores.save(score)

        # retrieve updated record
        score = scores.find_one({'student':1, 'type':'exam'})
        print 'after: ', score
    except:
        print 'Unexpected error: ', sys.exc_info()[0]
        raise

# replaces document wholesale
def using_update():
    
    db=connection.test
    scores=db.scores
    print 'updating record using update'

    try:
        score = scores.find_one({'student':1, 'type':'exam'})
        print 'before: ', score

        # add review date
        score['review_date'] = datetime.datetime.utcnow()

        # update rcord with update.  NB:  the record has an _id but
        # the DB is 'ok' with that b/c it matches the _id already there
        scores.update({'student':1, 'type':'exam'}, score)

        # retrieve updated record
        score = scores.find_one({'student':1, 'type':'exam'})
        print 'after: ', score
    except:
        print 'Unexpected error:', sys.exc_info()[0]
        raise

def using_set():

    db=connection.test
    scores=db.scores
    print 'updating record using set'

    try:
        score = scores.find_one({'student':1, 'type':'exam'})
        print 'before: ', score

        # update using set
        scores.update({'student':1, 'type':'exam'},
                    {'$set':{'review_date':datetime.datetime.utcnow()}})

        score = scores.find_one({'student':1, 'type':'exam'})
        print 'after: ', score
    except:
        print 'Unexpected error: ', sys.exc_info()[0]
        raise


remove_review_date()
using_save()
remove_review_date()
using_update()
remove_review_date()
using_set()
