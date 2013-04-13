import pymongo
import sys

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

# get your db handle
db = connection.students
grades = db.grades

# get all students homework scores

def remove_lowest_homework():
    query = { 'type' : 'homework' }
    selector = { 'student_id' : 1 , 'score' : 1, '_id' : 0 }

    try:
        homeworks = grades.find(query).sort([['student_id', pymongo.ASCENDING], ['score', pymongo.ASCENDING]])
    except:
        print 'Query failed: ', sys.exc_info()[0]

    for rec in homeworks:
        print rec

remove_lowest_homework()
