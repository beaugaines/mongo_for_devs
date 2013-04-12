import pymongo
import sys

from pymongo import MongoClient

# establish a connection to the db
connection = MongoClient('localhost', 27017)

db = connection.test
people = db.people

print 'insert, at your service'

achmed = {'name': 'Achmed Kandirali', 'company': 'Aleppo Soaps', 'interests': ['sheesha', 'schwarma', 'baksheesh']}

pierre = {'name': 'Pierre Rochfoucauld', 'company': 'La Fete d\'Ane', 'interests': ['cantal bien fait', 'bricolage', 'spelunc']}


try:
    people.insert(achmed)
    people.insert(richard)

except:
    print 'Mysterious error: ', sys.exc_info()[0]
    