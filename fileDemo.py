#-*-coding:utf-8-*-

#文件的操作
'''
打开文件的格式：file = open(file_name,mode)，使用file.read()和file.close(),
可以打开和关闭文件file，其中，mode有5种：r、w、a、+、b，a表示以追加的方式，
既，每次写的时候，都写在上次的后面，a+表示如果文件不存在，先创建在写。
read()表示全部读取，返回值为字符串；readline()表示只读取一行，返回值为字符串
readlines()表示读取多行，返回值为列表。在linux系统中，readline()返回时将在后面
加上'\n'
'''
import itertools
#文件的读操作
file = open('temp.txt','r')
f1 = file.read()
print file,'\n',f1,'\n'
file.close()

file = open('temp.txt','r')
f2 = file.read(5)
print f2,'\n'
file.close()

file = open('temp.txt','r')
L1 = file.readline()
L1 =L1.rstrip('\n')
L2 = file.readline()
print L1
print L2,'\n'
file.close()

file = open('temp.txt','r')
L = file.readlines()
print L
file.close()

'''
文件的写操作使用到的函数有：write()和writelines()，其中，write()传入的参数是
字符串，writelines()传入的参数是序列
'''
#文件的写操作
f0 = open('test_1.txt','w')
a = 'Hello'
b = 'world !'
c = 'www.baidu.com'
f1 = f0.write(a)
f2 = f0.write(b)
f3 = f0.write(c)
f0.close()

f0 = open('test_2.txt','w')
a = 'Hello'
b = 'world !\n'
c = 'www.baidu.com'
f1 = f0.write(a + '\n')
f2 = f0.write(b)
f3 = f0.write(c)
f0.close()

f0 = open('test_3.txt','w')
f1 = f0.writelines([a+'\n',b,c])
f0.close()

f2 = open('test_3.txt','r')
f3 = f2.readlines()
print f2,'\n',f3 
print 'the end'
f2.close()

#文件的格式化写操作
f0 =open('format.txt','w')
a = '%10s%14s%16s\n' %('Id','name','record')
b = '%10d%14s%16.2f\n' %(100,'John',98.2345)
c = '%10d%14s%16.2f\n' %(101,'Tom',88.345)
'''f1 = f0.write(a)
f2 = f0.write(b)
f3 = f0.write(c)'''
f0.writelines([a,b,c])
f0.close()

#使用while和for循环实现文件的读操作
f0 = open('format.txt','r')
s1 = f0.readline()
while s1 != '':
    s1 = s1.rstrip('\n')
    print s1
    s1 = f0.readline()
f0.close()
print 'while end'

f0 = open('format.txt','r')
for i in f0:
    s1 = i.rstrip('\n')
    print s1
f0.close()
print 'the end for'

f0 = open('format.txt','r')

f1 = iter(f0)
print f1.next(),
print f1.next(),
print f1.next()
f0.close()