#-*-coding:utf-8-*-

#list使用

''' list可以修改、动态增加长度,可以使用help(list)查看可以操作的函数'''

s = [1,2,3,'asd','q',6,[7,8,9]]
h = ['a',0,'w','m','y']
s1 = s[3].replace('d',s[4])
print s,'\n',s1

s2 = s[2:5]
print s2

print s[6][1] #将S列表中的index为6的项：[7,8,9]中的index为1的项取出

a = s + h
print 's= ',s,'\n','h= ',h,'\n','a=s+h ',a

#添加元素、指定位置插入元素
a = h.append('f')
print h
b = h.insert(0,'p')
print h

s = range(1,10)
a = s.index(3)
print s,'\n',a

#list的添加
a = ['a','b','c']
s.append(a)  #仅仅将要添加的元素作为一个整体添加到list中
s.extend(a) #通过iterator先将添加的list的值取出来，在作为一个整体添加到list中
print s,'\n',s

#count()用来统计列表中某个元素出现的次数
a = [1,2,3,4,5,6]*2
i= a.count(3)
print 'a= ',a,'\n',i

a.remove(1) #仅仅删除列表中第一次出现的元素
print a

del a[0]
print a

a.__delitem__(2) #__delitem__()是list内置函数等同于del a[index]
print a

a = [1,2,3,4,5,6]
print a
a1 = a.pop(a.index(4)) #pop()函数表示将list中指定的元素删除，并返回删除的值
print a,'\n',a1

b = [1,2,3,4,5,6]
print b
b.reverse() #reverse()表示将list逆序
print b