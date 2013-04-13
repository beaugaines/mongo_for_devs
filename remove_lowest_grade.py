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

    try:
        homeworks = grades.find(query).sort([['student_id', pymongo.ASCENDING], ['score', pymongo.ASCENDING]])
    except:
        print 'Query failed: ', sys.exc_info()[0]


    index = 0
    for rec in homeworks:
        if index == rec['student_id']:
            grades.remove(rec)
            index +=1


