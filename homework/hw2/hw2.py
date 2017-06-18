# take a dataset, filter on type and remove the lowest value
"""
Created on Sat Jun 10 22:38:47 2017

@author: mckinns
"""

import pymongo
# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
        
# removes one student
def rem_low():
    # get a handle to the database
    db=connection.back_students
#    db=connection.students
    grades = db.grades

    print "find(), reporting for duty"
  #  filter = {'type':'homework', 'student_id':{'$lt':3}}
  #  filter = {'type':'homework', 'student_id':7}
    filter = {'type':'homework'}
    stud = ''
    
    try:
    #a cursor returned as many elements
        cursor = grades.find(filter)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),
                              ('score', pymongo.ASCENDING)])
    except Exception as e:
        #into a try/error block
        print "Unexpected error:", type(e), e

    x_id = ''
    # have a count to limit the returned rows
    for doc in cursor:
        if (doc['student_id'] != stud):
            stud = doc['student_id']
            x_id = doc['_id']
            result = grades.delete_one({'_id':x_id})
   #     else:
    #        print "match"
     #       print doc
       #     stud = doc['student_id']            