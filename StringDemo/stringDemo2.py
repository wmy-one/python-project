#-*-coding:utf-8-*-

#�ַ����ķ�������

'''
�����ַ������ȵĺ���len(),���磺len(str_name)��ȡ�������ַ���ASCLL��������ord(),
���磺ord(a)��᷵��97��Ҳ���Լ���ASCLL��Ӧ���ַ�����Ϊchr()������ַ������׻�β
���пո�����ǲ�����ո������ʹ�ú���strip()��ȥ����ո�(�ײ�)����lstrip()��
ȥ���ҿո�(β��)����rstrip()�����һ���ַ��������ض����ַ�����ţ�����Խ���Щ
�ض����ַ��������Ϊ�ָ�����������ַ����ֳ����С�Σ�����ʹ�ú���split(),Ĭ��
�ÿո�ָ������磺str_name.split('.')��split()����ֵΪlist���͡�
��������ĳ���ַ������Ƿ���ĳ�ַ���������ʹ�ú���find()��Ĭ�ϴ������Ҳ飬
Ҳ����ʹ�ô������Ҳ�ĺ���lfind()�����������ĺ���Ϊrfind()��
���磺str_1.find('str_2')������ֵΪ��һ�β鵽�ַ���str_2��index
'''

s0 = '  www.baidu.com a  ds ' #ʹ��strip()��������ȥ���׺�β�Ŀո�
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

#isalnum()��ʾ�ж�һ���ַ����Ƿ�����ĸ���������
a = 'a1b2c3'
print a.isalnum()

#isalpha()��isdigit()�ֱ��ж��Ƿ��ɴ���ĸ���������
a = 'abc'
b = '123'
c = '123abc'
print a.isalpha(),b.isdigit(),c.isalpha(),c.isdigit()

#islower()��isupper()��ʾ�ж��ַ����Ƿ�ȫΪ��д��Сд
#lower()��upper()��ʾ�ֱ��ַ����е��ַ�СдתΪ��д����дתΪСд
a = 'ASD'
b = 'asd'
c = 'asdASD'
print a.isupper(),b.islower(),c.upper(),c.lower()

#isspace()��ʾ�Ƿ�Ϊ���ַ���replace(old,new)��ʾ���ַ����е�old�滻Ϊnew
'''replace()�滻ԭ�����Ƚ�ԭ�ַ���copyһ�ݣ����滻��ԭ�ַ�������'''
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
