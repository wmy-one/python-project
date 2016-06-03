#-*-coding:utf-8-*-

#自定义一个my_split()方法，实现字符串的分隔

s1 = 'asd*qwe*123**zxc'
s2 = '1asd**2qwe**3zxc***4abc'
s3 = '1qwe***2asd***3zxc**123'
s4 = '***1asd**2qwe**3zxc***4abc'
s5 = '**asd'
s6 = 'asd'
#s3 = '***1qwe***2asd***3zxc**123'
c = s4.find('**')
print c
def my_split(str,sep):
    n = len(sep)
    a = str.find(sep)
    if a !=0 and a == -1:
        print str
    elif a != 1:
        print str[:a]
    #elif str[a:a+n] == sep:
        #a = a+n
    
    #print str[:a]
    b = a
    while b <= len(str) and b != -1:
        while str[a:a+n] == sep:
            a = a + n
        b = str.find(sep,a)
        if b != -1:
            print str[a:b]
        else:
            print str[a:]
        a = b

print 'The beginning of my_split():'
my_split(s1,'*')
print 'out of s1'
my_split(s2,'**')
print 'out of s2'
my_split(s3,'***')
print 'out of s3'
my_split(s4,'**')
print 'out of s4'
my_split(s5, '**')
print 'out of s5'
my_split(s6, '*')
print 'The stop of my_split()'
#如何将上述冗余的函数调用简化呢？使用字典dic()函数如何实现？

#实现与python本身的split()方法相同的功能
s0 = '1qwe**2asd****3zxc******4abc'
def my_split_same(str,sep):
    a = str.find(sep)
    b = str.find(sep)
    print a,b
    print str[:a]
    while b != -1:       
        a = str.find(sep,b)
        b = str.find(sep,a + len(sep))
        if b - a == len(sep):
            print '\'\''            
        elif b != -1:
            print str[a + len(sep):b]
        else:
            print str[a + len(sep):]
            
w = '**'
print s0.split(w)
my_split_same(s0,w)
print 'stop'
            