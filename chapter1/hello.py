import bottle
import pymongo

# this is the handler for the default path of the webserver

# NH - next function is going to be executed when this route is hit0
@bottle.route('/')
# NH - there is nothing special about the word index, this could be called anything
def index():

    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.test


    # get handle for names collection
    name = db.names

    # find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)