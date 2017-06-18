#  3.1 - 
# take a dataset, filter on type and remove the lowest value within a nested array
"""
Created on Sun Jun 18 14:49:01 2017

@author: mckinns
"""
import pymongo
connection = pymongo.MongoClient("mongodb://localhost")

# removes one student
def array_low():
    # get a handle to the database
    db=connection.school
    students = db.students
    # list to gather up score and filter for min
    stud_score = []
    i = 0    

    try:
    #a cursor returned as many elements
        cursor = students.find()
        
    except Exception as e:
        #into a try/error block
        print "Unexpected error:", type(e), e
                
    for doc in cursor:
        print doc['scores']
            
        while (i < len(doc['scores'])):
            if (doc['scores'][i]['type'] =='homework'):
                stud_score.append(doc['scores'][i]['score'])
            
            i = i + 1
 
        min_score =  min(stud_score)
# update the collection
        students.update({'_id': doc['_id']}, {'$pull': {'scores': {'score': min_score}}})
        
        stud_score = []   
        i = 0
    
