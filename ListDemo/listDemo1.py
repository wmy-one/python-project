#-*-coding:utf-8-*-

#listʹ��

''' list�����޸ġ���̬���ӳ���,����ʹ��help(list)�鿴���Բ����ĺ���'''

s = [1,2,3,'asd','q',6,[7,8,9]]
h = ['a',0,'w','m','y']
s1 = s[3].replace('d',s[4])
print s,'\n',s1

s2 = s[2:5]
print s2

print s[6][1] #��S�б��е�indexΪ6���[7,8,9]�е�indexΪ1����ȡ��

a = s + h
print 's= ',s,'\n','h= ',h,'\n','a=s+h ',a

#���Ԫ�ء�ָ��λ�ò���Ԫ��
a = h.append('f')
print h
b = h.insert(0,'p')
print h

s = range(1,10)
a = s.index(3)
print s,'\n',a

#list�����
a = ['a','b','c']
s.append(a)  #������Ҫ��ӵ�Ԫ����Ϊһ��������ӵ�list��
s.extend(a) #ͨ��iterator�Ƚ���ӵ�list��ֵȡ����������Ϊһ��������ӵ�list��
print s,'\n',s

#count()����ͳ���б���ĳ��Ԫ�س��ֵĴ���
a = [1,2,3,4,5,6]*2
i= a.count(3)
print 'a= ',a,'\n',i

a.remove(1) #����ɾ���б��е�һ�γ��ֵ�Ԫ��
print a

del a[0]
print a

a.__delitem__(2) #__delitem__()��list���ú�����ͬ��del a[index]
print a

a = [1,2,3,4,5,6]
print a
a1 = a.pop(a.index(4)) #pop()������ʾ��list��ָ����Ԫ��ɾ����������ɾ����ֵ
print a,'\n',a1

b = [1,2,3,4,5,6]
print b
b.reverse() #reverse()��ʾ��list����
print b