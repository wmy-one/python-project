#!usr/bin/evn python 

'''
This python will realize get oddnum and evennum from a range(20).
build a func to judge two num whether one devide other
'''

s = range(20)
print 's = ',s

s1 = []
s2 = []
for i in s:
    if i % 2:
        s1.append(i)
    else:
        s2.append(i)

print "The odd part of 's' is :"
print s1
print "The even part of 's' is :"
print s2
print '*' * 50

a = int(raw_input('Please input the first num :'))
b = int(raw_input('Please input the second num :'))

def devide(i,j):
    if i % j:
        print 'False'
    else:
        print 'True'
devide(a,b)
