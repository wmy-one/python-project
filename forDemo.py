#-*-coding:utf-8-*-

#forѭ����ʹ��

'''
��python�У�forѭ���ĸ�ʽΪ��for target in sequences������sequences(����)
�����������֣�list��tuple��string��file����ȡ�ļ��ĺ�����
open('file_name','�򿪷�ʽ').read()�����У�dearline()����ȡ�ļ��ĵ�һ�У�
read()��ȡ�����ļ��������ߵķ���ֵ��Ϊ�ַ������ͣ�
readlines()���Զ�ȡ�����ļ�������ֵΪlist
'''

#�ַ�����ʹ��
s1 = 'www.baidu.com'
for a in s1:
    print a
else:
    print 'out of for_string'

#�б��ʹ��
s2 = [1,2,3,4,'w',3.14]
for b in s2:
    print b 
else:
    print 'out of for_list'
    
#Ԫ���ʹ��
s3 = (1,2,3,4,'w',3.14)
for c in s3:
    print c
else:
    print 'out of for_tuple'

#�ļ���ʹ��
s4 = open('__init__.py','r').read()
for d1 in s4:
    print d1
    open('temp_1.txt','a+').write(d1)
else:
    print 'out of for_file_read()'

s5 = open('__init__.py','r').readline()
for d2 in s5:
    print d2
    open('temp_2.txt','a+').write(d2)
else:
    print 'out of for_file_readline()'

s6 = open('__init__.py','r').readlines()
for d3 in s6:
    print d3
    open('temp_3.txt','a+').write(d3)
    open('temp_4.txt','w').write(d3)
else:
    print 'out of for_file_readlines'
