import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.school

# this queyr works in the mongo shell
# students = db.students.aggregate({ $unwind: "$scores"},
# { $match : { 'scores.type' : 'homework'}}, {$sort: {'name':1, 'scores.score':-1}})


scores = db.students.aggregate([{ '$unwind': "$scores"},
    { '$match' : { 'scores.type': 'homework' }},
    { '$group' : { '_id': '$_id', 'low_score': { '$min' : '$scores.score'}}}])


for res in scores['result']:
    db.students.update( { '_id': res['_id']},
            { '$pull' : { 'scores': { 'score': res['low_score'] } } })




