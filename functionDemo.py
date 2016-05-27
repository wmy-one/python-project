#-*-coding:utf-8-*-

#自定义一个函数，且这个函数有多个返回值

'''
m3 = fun_a(a=1,2,c=6)、m4 = fun_a(1,2,b=6)和m5 = fun_a(1,b=2,6)这样写均报错
①python语法中，无赋值的实参必须放在赋值的实参之前；
②在多个无赋值的实参中，第一个实参默认赋值给函数中第一个形参；
③即使后面仍然写着给第二个实参赋值，仍然会将第二个实参赋值给第二个形参；
'''

def fun_test(a,b):
    print a,' ',b
    s1 = a + b
    s2 = a - b
    s3 = a * b
    s4 = a / b
    s5 = a % b
    s6 = a / float(b)
    s7 = a ** b
    return s1,s2,s3,s4,s5,s6,s7

def fun_a(a,b,c=3):
    print a,b,c
    sum = a + b +c
    return sum

#第一种调用函数
re = fun_test(2,4) #函数的返回值有多个时，而赋值变量仅为一个，则会生成一个tuple
print re

#第二种调用函数
n1,n2,n3,n4,n5,n6,n7 = fun_test(2,4)
print n1,' ',n2,' ',n3,' ',n4,' ',n5,' ',n6,' ',n7

#第三次调用函数
for i in fun_test(2,4):
    print i,' ',
print '\n'    

#调用函数：fun_a()
n = fun_a(1,2)
m = fun_a(1,2,6)
print n,m

m1 = fun_a(1,c=2,b=6)
print 'm1= ',m1

m2 = fun_a(c=1,b=2,a=6)
print 'm2= ',m2
