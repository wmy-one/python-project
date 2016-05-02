#!/usr/bin/env python

'''According a special format output the payment !'''

a = float(raw_input('Entry the balance :'))
b = float(raw_input('Entry the payment :'))

print 'Entry the balance: $%.2f' % a
print 'Entry the payment: $%.2f' % b

print '%6s%10s%12s' % ('num','paid','balance')
print '%6s%10s%12s' % ('*'*5,'*'*6,'*'*8)

def Payment(x,y):
    i = 0
    m = 0
    n = x
    while y <= x or x > 0:

        print '%5d%6s%.2f%7s%.2f' % (i, '$', m, '$', n)
        i = i + 1
        m = y
        n = x - m
        x = n
    else:
        m = n + y
        n = x + y - m
        print '%5d%6s%.2f%7s%.2f' % (i, '$', m, '$', n)

Payment(a, b)

