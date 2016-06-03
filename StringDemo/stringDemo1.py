#-*-coding:utf-8-*-
#字符串的格式化输出、 索引、切片、重复(*)、连接(+)

'''
字符串的格式化输出的格式为：‘name:%s,sex:%s,record:%d’ %('Jhon','male',88)
其中，前面的字符串可以用单引号或双引号均可；索引操作：str_name[index]字符串
的第一个字符的index为0，最后一个字符的index可以用-1也可以用len(str_name)-1表示。
连接：str_1 + str_2 ,且‘+’前后均为字符串，若为其他类型需转换为字符串，重复是连接
的叠加操作，例如：‘a' * 3，表示将a重复3次；切片操作：str_name[start:stop:step],
其中，step默认为1，可以为负数，表示从右向左切(index所在处字符的右边切)，输出倒序，
正数表示从左向右切(index所在处字符的左边切)，输出正序。
'''
s1 = '1234567890'
s2 = 'abc'

#格式化输出操作
print 'name:%s, sex:%s, record:%d' %('Jhon','male',99)

#连接和重复操作
a = s1 + s2 + str(8)
b = s2 * 3
print a,b

#索引操作
print s1[2],s1[-1],s2[0]

#切片操作
a = s1[0:8]
b = s1[:-1]
c = s1[-1::-1]
d = s2[2::-1]
e = s2[2:0:-1]
f = s1[0:-1:2]
print a,b,c,d,e,f 