#-*-coding:utf-8-*-

#��һ����һ�������ո�ָ���ַ����У�ȡ��ȫ���ĵ���

'''
����һ�������ո�ָ���ַ����У�ȡ��ȫ���ķָ�ʣ���ô�죿
����һ��ʹ��str_name.split()�������ʵ��
��������
����ʹ��str_name.strip()ȡ���ַ���str_name���׺�β�Ŀո�
�ڴ���߿�ʼ���ҵ�һ���ո�������ţ��޽���Ѱ��
���ҵ�(��һ���ո�����)��һ���ѿո��ַ���index
���ظ��ڡ����۲���
ʹ��find()���������ַ���ʱ����û�ҵ����򷵻�ֵΪ-1
'''

s1 ="""  1asd 2a123   3qwe      4wmy   
  5zxc   6def  
"""

s2 = s1.strip()
print s2

#ȡ����һ������
a = s2.find(' ')
print s2[:a]

b = a
#ȡ��֮��ĵ���
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