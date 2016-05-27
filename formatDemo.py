# -*- coding:utf-8 -*-
#本次实验将会讲解，python的格式化输出和调用输入函数raw_input()
#如果想要添加中文注释或者输出中文，则需要在程序的第一行或脚本中的
#第一行或第二行添加上面的语句

'''
格式化输出语句：print(format(val,'m.nf')或print(format(val,'m.n%))
其中，m表示输出的位数，n表示小数后的位数；如果m大于输出的总长度，则右对齐，
否则左对齐，且保证正确的输出结果。
raw_input()函数从键盘输入读取数据，它的返回值为字符串，可以使用int()和float()
将结果强制转换为整型和浮点型数据；可以使用type()函数查看数据的类型
'''
print ''' 1表示m=3，n=2,输出小数和百分数：
 2表示m=6,n=2,输出小数和百分数：
 3表示m=6,n=4,输出小数和百分数：
 4表示调用输入函数raw_input():
 5表示将输入转换为整型数据：
 6表示将输入转换为浮点型数据：
'''
b = 3.1415
d = '123'
a = raw_input('please input number: ')
if a.endswith('one'):
    print(format(b,'3.2f'))
    print(format(b,'3.2%'))
elif a.endswith('two'):
    print(format(b,'6.2f'))
    print(format(b,'6.2%'))
elif a.endswith('three'):
    print(format(b,'6.4f'))
    print(format(b,'6.4%'))
elif a.endswith('four'):
    c=raw_input('请输入一个数字：')
    print c
elif a.endswith('five'):
    print(int(d))
elif a.endswith('six'):
    print(float(d))
