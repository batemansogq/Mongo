# https://university.mongodb.com/courses/MongoDB/M101P/2017_May/courseware/Chapter_1_Introduction/52547788e2d4231cc6083fdf/vertical_16785828a3ec
"""
Created on Wed May 31 21:23:28 2017

@author: mckinns
"""

# mongo shell
# db.names.insert({"name" : "scott"})

import pymongo

from pymongo import MongoClient

#connect
connection = MongoClient('localhost', 27017)

db = connection.test

#handle the collection
names = db.names

item = names.find_one()

# reference the field key
print item['name']
