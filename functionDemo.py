#-*-coding:utf-8-*-

#�Զ���һ������������������ж������ֵ

'''
m3 = fun_a(a=1,2,c=6)��m4 = fun_a(1,2,b=6)��m5 = fun_a(1,b=2,6)����д������
��python�﷨�У��޸�ֵ��ʵ�α�����ڸ�ֵ��ʵ��֮ǰ��
���ڶ���޸�ֵ��ʵ���У���һ��ʵ��Ĭ�ϸ�ֵ�������е�һ���βΣ�
�ۼ�ʹ������Ȼд�Ÿ��ڶ���ʵ�θ�ֵ����Ȼ�Ὣ�ڶ���ʵ�θ�ֵ���ڶ����βΣ�
'''

def fun_test(a,b):
    print a,' ',b
    s1 = a + b
    s2 = a - b
    s3 = a * b
    s4 = a / b
    s5 = a % b
    s6 = a / float(b)
    s7 = a ** b
    return s1,s2,s3,s4,s5,s6,s7

def fun_a(a,b,c=3):
    print a,b,c
    sum = a + b +c
    return sum

#��һ�ֵ��ú���
re = fun_test(2,4) #�����ķ���ֵ�ж��ʱ������ֵ������Ϊһ�����������һ��tuple
print re

#�ڶ��ֵ��ú���
n1,n2,n3,n4,n5,n6,n7 = fun_test(2,4)
print n1,' ',n2,' ',n3,' ',n4,' ',n5,' ',n6,' ',n7

#�����ε��ú���
for i in fun_test(2,4):
    print i,' ',
print '\n'    

#���ú�����fun_a()
n = fun_a(1,2)
m = fun_a(1,2,6)
print n,m

m1 = fun_a(1,c=2,b=6)
print 'm1= ',m1

m2 = fun_a(c=1,b=2,a=6)
print 'm2= ',m2
