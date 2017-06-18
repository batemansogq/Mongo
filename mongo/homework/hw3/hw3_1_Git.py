# https://github.com/ladamalina/M101P/blob/master/HW3.1/script.py
"""
Created on Sun Jun 18 16:37:49 2017

@author: mckinns
"""

import pymongo
import sys


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school                 # attach to db
collection = db.students         # specify the colllection

try:
    iter = collection.find({'scores.type': 'homework'})
    for item in iter:
        min_hw_score = 101
        
        for score in item['scores']:
             if score['type'] == 'homework' and score['score'] < min_hw_score:
                 min_hw_score = score['score']
        
        if min_hw_score < 101:
            collection.update({'_id': item['_id']}, {'$pull': {'scores': {'score': min_hw_score}}})
except:
    print "Error:", sys.exc_info()