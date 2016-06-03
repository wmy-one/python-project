#-*-coding:utf-8-*-

#从一段由一个或多个空格分割的字符串中，取出全部的单词

'''
想由一个或多个空格分割的字符串中，取出全部的分割单词，怎么办？
方法一：使用str_name.split()，便可以实现
方法二：
①先使用str_name.strip()取出字符串str_name的首和尾的空格
②从左边开始查找第一个空格的索引号，无结束寻找
③找到(第一个空格后面的)第一个费空格字符的index
④重复②——③操作
使用find()函数查找字符串时，做没找到，则返回值为-1
'''

s1 ="""  1asd 2a123   3qwe      4wmy   
  5zxc   6def  
"""

s2 = s1.strip()
print s2

#取出第一个单词
a = s2.find(' ')
print s2[:a]

b = a
#取出之后的单词
while b <= len(s2) and b != -1:
    while s2[a] == ' ':
        a = a + 1
    else:
        print 'a= ',a,s2[a]
    b = s2.find(' ',a)
    if b != -1:
        print s2[a:b]
    else:
        print s2[a:]
    a = b
    
s1 = ' asd '
s2 = ' asd'
a = s1.find(' ',1)
b = s2.find(' ',1)
print a,b