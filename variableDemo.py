# -*- coding:utf-8 -*-
#python语言的变量使用
'''
python语言的变量不用声明数据类型，可以直接赋值，既，给变量赋什么类型的数据，
变量的数据类型就是什么数据类型；赋值后，python的变量指向该数据所在内存单元的地址，
当重新给变量赋值时，该变量又指向了新的数据所在的内存单元的地址。可以使用id()函数
查看变量指向的内存单元的地址
'''
a = 12
b = 13
print 'a= ',a, id(a)
print 'b= ',b, id(b)

a=b
print 'a= ',a, id(a)
print 'b= ',b, id(b)

a=15
b=16
print 'a= ',a,id(a)
print 'b= ',b,id(b)