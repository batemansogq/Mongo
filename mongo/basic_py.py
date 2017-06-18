# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 21:18:56 2017

@author: mckinns
"""

#=================================================================
#basic loop
sum = 0
numbers = [1, 2, 3, 5, 8]
for i in numbers:
    sum = sum + i

print sum
#=================================================================
#loop a dict
people = {'name': 'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}

for item in people:
    if (item == 'favorite_color'):
        print people[item]
        
#=================================================================
#while loop
f = ['a','b','c']

i = 0
while (i < len(f)):
    print f[i]
    i = i + 1
    
#=================================================================
# functions

f = ['a','b','c','b','c','b','c']

def analysis(l):
    counts={}
    for item in l:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    
    return counts

counts = analysis(f)
print(counts)

#=================================================================
# error handling
import sys

try:
    print 5 / 0
except Exception as e:
    print "exception: ", type(e), e

print "but life goes on"

    
    