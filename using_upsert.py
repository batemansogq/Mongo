
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
things = db.things

def using_upsert():

    print "updating with upsert"

    try:

        # lets remove all stuff from things
        things.drop()
            #cant find match, so insert
        things.update_one({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
           #cant find match, so insert
	things.update_many({'thing':'banana'}, {'$set':{'color':'yellow'}}, upsert=True)
           #cant find match, so insert only 'color':'green'
           #would require {'thing':'pear','color':'green'} to full doco insert
        things.replace_one({'thing':'pear'}, {'color':'green'}, upsert=True)


        apple = things.find_one({'thing':'apple'})
        print "apple: ", apple
        banana = things.find_one({'thing':'banana'})
        print "banana: ", banana 
        pear = things.find_one({'thing':'pear'})
        print "pear: ", pear

    except Exception as e:
        print "Unexpected error:", type(e), e
        raise




using_upsert()
