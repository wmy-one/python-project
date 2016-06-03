#-*-coding:utf-8-*-

#字符串的方法操作

'''
计算字符串长度的函数len(),例如：len(str_name)；取出单个字符的ASCLL，可以用ord(),
例如：ord(a)则会返回97，也可以计算ASCLL对应的字符函数为chr()；如果字符串的首或尾
含有空格，输出是不想带空格，则可以使用函数strip()，去除左空格(首部)函数lstrip()，
去除右空格(尾部)函数rstrip()；如果一段字符串内由特定的字符或符号，则可以将这些
特定的字符或符号作为分隔符，将这段字符串分成许多小段，可以使用函数split(),默认
用空格分隔，例如：str_name.split('.')，split()返回值为list类型。
如果想查找某段字符串中是否含有某字符串，可以使用函数find()，默认从左向右查，
也可以使用从左向右查的函数lfind()，从右向左查的函数为rfind()，
例如：str_1.find('str_2')，返回值为第一次查到字符串str_2的index
'''

s0 = '  www.baidu.com a  ds ' #使用strip()函数仅仅去除首和尾的空格
s1 = ' www.baidu.com '
s2 = '123456abc123456abc'
s3 = 'abc'
a = s1.strip()
b = s1.rstrip()
c = s1.split('.')
d = s2.find(s3)
e = s2.rfind(s3)
f = s2.find(s3,7)

print a
print b
print s0.strip()
print c,d,e,f

#isalnum()表示判断一个字符串是否由字母和数字组成
a = 'a1b2c3'
print a.isalnum()

#isalpha()和isdigit()分别判断是否由纯字母、数字组成
a = 'abc'
b = '123'
c = '123abc'
print a.isalpha(),b.isdigit(),c.isalpha(),c.isdigit()

#islower()和isupper()表示判断字符串是否全为大写、小写
#lower()和upper()表示分别将字符串中的字符小写转为大写，大写转为小写
a = 'ASD'
b = 'asd'
c = 'asdASD'
print a.isupper(),b.islower(),c.upper(),c.lower()

#isspace()表示是否为空字符，replace(old,new)表示将字符串中的old替换为new
'''replace()替换原理，是先将原字符串copy一份，在替换，原字符串不变'''
a = ''
b = ' 1a'
c = ' '
d = 'asdqwezxc'
e = d.replace('qwe','qwe'.upper())
print a.isspace(),b.isspace(),c.isspace()
print d,e
print id(d),id(e)

s0 = 'asd123?!*'
s1 = 'abcASD'
s2 = s1.lower().upper()
print s0.isalnum(),s0.isalpha(),s0.isdigit()
print s1,s2,s0.upper()

for a in s0:
    print a,
