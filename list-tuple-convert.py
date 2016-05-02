#!/usr/bin/env python

'''
This python programmer will show the real feature of converting between list and tuple by invoking id() func.
'''

s1 = [1,2,3]
s2 = (4,5,6)

print '*'*30
print 'member(s1)','|',' s1_id','|','s2_id ','|','member(s2)'
for j in range(3):
    print '%11d|%d|%d|%3d' % (s1[j], id(s1[j]), id(s2[j]), s2[j])

# The convert list to tuple
s3 = tuple(s1)
print '*'*30
print 'The result of convert list to tuple: ',s3
print 'The list id() and tuple id(): '
print '*'*30

print 'member(s1)','|',' s1_id','|','s3_id '
for i in range(3):
    print '%11d|%d|%d' % (s1[i],id(s1[i]),id(s3[i]))

s4 = list(s2)
print '*'*30
print 'The result of convert tuple to list: ',s4
print 'The tuple id() and list id(): '
print '*'*30

print 'member(s2)','|',' s2_id','|','s4_id '
for i in range(3):
    print '%11d|%d|%d' % (s2[i],id(s2[i]),id(s4[i]))
