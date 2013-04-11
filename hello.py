import bottle
import pymongo

# handler for default path of web server

@bottle.route('/')
def index():

   # connect to mongo
   connection = pymongo.MongoClient('localhost', 27017)

   # attach to test db
   db = connection.test

   # get handle for names collection
   name = db.names

   # find a single doc
   item = name.find_one()

   return '<b>Hello {0}</b>'.format(item['name'])

# start server
bottle.run(host='localhost', port=8082)
