#-*-coding:utf-8-*-

#list��Ϊ�������β�

s1 = list('www.baidu.com')
s = [1,2,3,4,5,6]

#�Զ���һ��ͳ��list����ĸ�ĸ����ĺ���
def list_pop(lis,sep):
    print lis
    while sep in lis:
        a = lis.pop(lis.index(sep))
        print a
    num_ch = len(lis)
    return num_ch

a = list_pop(s1,'.')
print 'in %s have %d char ' %(s1,a)
  

#�Զ���һ����������ĺ���
def my_reverse(lis):
    print lis
    return lis[::-1]

b = my_reverse(s)
print b


#��listд���ļ���
s = ['hello','world','bistu','abc',[1,2,3]]
s1 = range(1,10)
s2 = s + s1
s2.append(98.56)
s2.append('*')

f = open('test.txt','w')
i = 0
while i <= len(s2) - 1:
    if isinstance(s2[i],str):
        f.write(s2[i]+'\n')
    else:
        f.write(str(s2[i])+'\n')
    i = i + 1
f.close()
#���ʹlist�е�listԪ���е���Ҳ���������ĸ�ʽ����أ�����ʹ�õݹ麯��ʵ��

#ʹ��readlines()���ļ����䷵��ֵΪlist������ӡlist
f1 = open('test.txt','r')
a = f1.readlines()  #ʹ��readlines()ʱ�����ÿ�еĻ��з���'\n'��ȡ����

for i in a:
    i = i.rstrip('\n')
    print i
    
f1.close()
    
''' �ٴ��͢ڴ����ļ��ĳ�������𣺷��ڢٴ���ִ�н��Ϊ�������[1,2,3]�е�Ԫ�أ�
Ȼ���ٴ�ͷ��β(ȥ��[1,2,3])���s0�е�Ԫ�أ����ڢڴ�����������˳���������������
��˼άϰ�ߡ�
���ڢٴ���ִ��˳��������ǵ�˼άϰ�ߣ���������ȴ��ͬ��Ϊ���أ�
ԭ��Ϊ�����ڢٴ���ִ�е�[1,2,3]��ʱ���ִ���һ���ļ�����һ���򿪵��ļ���û�йرգ�
[1,2,3]ִ����󣬲Źر���򿪵��ļ����ٹر�s0�򿪵��ļ��������ͻ����������˵��
�����������ڢڴ���ÿ��ִ��һ���������͹ر�һ���ļ����������Լ�ʱ�ı����ļ���
'''

#�ݹ麯��
def list_ch(lis_1):
    print lis_1
    
    #f2 = open('test_1.txt','w') #��
    i = 0
    while i <= len(lis_1) - 1:
        
        f2 = open('test_1.txt','a') #��
        
        if isinstance(lis_1[i],str):
            f2.write(lis_1[i] + '\n')
            print 'A1'
        elif isinstance(lis_1[i],list):
            a = list(iter(lis_1[i]))
            list_ch(a)
            print 'A2'
        else:
            f2.write(str(lis_1[i]) + '\n')
            print 'A3'   
                   
        i = i + 1            
        f2.close()
        print 'A4' 
    
s0 = ['hello','world','bistu',4,5,6,'abc',[1,2,3]]   
list_ch(s0)   
  
#���õݹ麯��ʵ��list�е�listԪ���е����ͬ����ʽ���
