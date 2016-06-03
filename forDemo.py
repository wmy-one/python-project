#-*-coding:utf-8-*-

#for循环的使用

'''
在python中，for循环的格式为：for target in sequences：其中sequences(序列)
的类型有四种：list、tuple、string、file；读取文件的函数：
open('file_name','打开方式').read()，其中，dearline()仅读取文件的第一行，
read()读取整个文件，且两者的返回值均为字符串类型；
readlines()可以读取整个文件，返回值为list
'''

#字符串的使用
s1 = 'www.baidu.com'
for a in s1:
    print a
else:
    print 'out of for_string'

#列表的使用
s2 = [1,2,3,4,'w',3.14]
for b in s2:
    print b 
else:
    print 'out of for_list'
    
#元组的使用
s3 = (1,2,3,4,'w',3.14)
for c in s3:
    print c
else:
    print 'out of for_tuple'

#文件的使用
s4 = open('__init__.py','r').read()
for d1 in s4:
    print d1
    open('temp_1.txt','a+').write(d1)
else:
    print 'out of for_file_read()'

s5 = open('__init__.py','r').readline()
for d2 in s5:
    print d2
    open('temp_2.txt','a+').write(d2)
else:
    print 'out of for_file_readline()'

s6 = open('__init__.py','r').readlines()
for d3 in s6:
    print d3
    open('temp_3.txt','a+').write(d3)
    open('temp_4.txt','w').write(d3)
else:
    print 'out of for_file_readlines'
