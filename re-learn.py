#!/usr/bin/env python

import re

m1_0 = r'^([\w\_]+)@([\w]+).com$' 
m1 = r'^([\w\_]+)@([\w]+).([\w]+)$'
m2_0 = r'^(<([\w\.\s]+)\s([\w]+)>)[\w\_]+@([\w]+).com$'
m2 = r'^(<([\w\.\s]+)\s([\w]+)>)[\w\_]+@([\w]+).([\w]+)$'

my_re_email_1 = re.compile(m1_0)
my_re_email_2 = re.compile(m2)

s0 = 'wmy_one@163.com'
s1 = 'someone@gmaile.com'
s2 = '<Tom Jone>tom@microsoft.com'

print (my_re_email_1.match(s0))
print (my_re_email_1.match(s1))
print (my_re_email_2.match(s2))

while True:

    my_email = input('please enter your email: ')

    if my_re_email_1.match(my_email) or my_re_email_2.match(my_email):
        print ('you enter email is legal !')
    elif my_email == 'q':
#break
        print ('You will quit the programmer !')
        break
    else:
        print ('invalid input, try again !')

