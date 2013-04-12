
import pymongo

# get next num in sequence
def get_next_sequence_number(name):

    from pymongo import MongoClient

    # establish a connection to the db
    connection = MongoClient('localhost', 27017)

    # get your db handle
    db = connection.test
    counters = db.counters

    # hit me with a seq number!
    counter = counters.find_and_modify(query={'type':name},
                                        update={'$inc':{'value':1}},
                                        upsert=True, new=True) 

    counter_value = counter['value']

    return counter_value


print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')

