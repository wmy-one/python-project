#-*-coding:utf-8-*-

#if����while����ʹ��

a = int(raw_input('Please input your Chinese record: '))
if a >= 90:
    print 'A'
elif a >= 80:
    print 'B'
elif a >= 70:
    print 'C'
elif a >=60:
    print 'D'
else:
    print 'No pass !'
    
#1+2+����+100
i = 1
s = 0

while i <= 100:
    s = s + i
    i = i + 1
    if s == 6:
        print s
        break  #�˴���break������while����elseѭ���壬�����ǽ�����if���
else:
    print 'else of while !'
print 'out of while !'