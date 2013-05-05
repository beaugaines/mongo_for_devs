// Find comments author with most comments

db.posts.aggregate([ { '$unwind': '$comments' },
  { '$group': { '_id': '$comments.author', 'count': {'$sum': 1}} },
  { '$sort': {'count': -1} }, { '$limit': 1 } }
])


// find number of cities with population zero

db.zips.aggregate([ { '$match': { 'pop': 0} },
  { '$group': {_id:null, 'total_cities': {'$sum': 1}} } 
])

// find avg pop of cities in CA in NY with populations over 25,000

db.zips.aggregate([ { '$match': { 'state' : { '$in': ['NY', 'CA'] }}},
  { '$group': { _id: '$city', 'population': { '$sum': '$pop'}}},
  { '$match': { 'population': { '$gt': 25000 }}},
  { '$group': { _id: '$city', 'av_pop': { '$avg': '$population'} }}
])

// get best avg score of across a class, excluding quiz scores

db.grades.aggregate([
  { '$unwind': '$scores'},
  { '$match': 'scores.type': { '$ne': 'quiz'}},
  { '$group': { _id: {'student_id': '$student_id', 'class_id': '$class_id'},
    'average': { '$avg': '$scores.score'}}},
  { '$group': { _id: {'$id.class_id'}, 'class_average': { '$avg': '$average'} }},
  { '$sort': { 'class_average': -1 }},
  { '$limit': 1}
])

// find all cities that begin with a digit - whatever that means - and sum their population

db.zips.aggregate([
  { '$project': { 'population': '$pop'}, 'first_char': { '$substr': ['$city',0,1]}},
  { '$match': 'first_char', /\d/ },
  { '$group': { _id:null, 'total_pop': { '$sum': '$population'}}}
])