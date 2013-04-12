import json
import urllib2
import pymongo

from pymongo import MongoClient

# connect to db
connection = MongoClient('localhost', 27017)

# connect to reddit db - which does not exist, so - POOF! - it will be created
db = connection.reddit
stories = db.stories


url = 'http://www.reddit.com/r/technology/.json'
hdrs = { 'User-Agent' : 'Bob Dobbs' }
req = urllib2.Request(url, headers=hdrs)
reddit_page = urllib2.urlopen(req)

# get the phlegm clot of information that is the Reddit homepage
# http = urllib3.PoolManager()

# reddit_page = http.request('GET', 'http://www.reddit.com/r/technology/.json')

# parse json into python objects

parsed = json.loads(reddit_page.read())

# iterate through the items on the page

for item in parsed['data']['children']:
    # insert items into Mongo
    stories.insert(item['data'])