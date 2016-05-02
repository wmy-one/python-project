#!/usr/bin/python

a = 'Hello world !'

i = 0
for c in a:
    s = c
    if s == 'o':
        i = i + 1
        print "the time of 'o' : ",i
    print c
print a
