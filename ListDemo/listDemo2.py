#-*-coding:utf-8-*-

#list作为函数的形参

s1 = list('www.baidu.com')
s = [1,2,3,4,5,6]

#自定义一个统计list中字母的个数的函数
def list_pop(lis,sep):
    print lis
    while sep in lis:
        a = lis.pop(lis.index(sep))
        print a
    num_ch = len(lis)
    return num_ch

a = list_pop(s1,'.')
print 'in %s have %d char ' %(s1,a)
  

#自定义一个逆序输出的函数
def my_reverse(lis):
    print lis
    return lis[::-1]

b = my_reverse(s)
print b


#将list写入文件中
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
#如何使list中的list元素中的项也按照这样的格式输出呢？可以使用递归函数实现

#使用readlines()读文件，其返回值为list，并打印list
f1 = open('test.txt','r')
a = f1.readlines()  #使用readlines()时将会把每行的换行符：'\n'读取出来

for i in a:
    i = i.rstrip('\n')
    print i
    
f1.close()
    
''' ①处和②处打开文件的程序的区别：放在①处，执行结果为：先输出[1,2,3]中的元素，
然后再从头到尾(去除[1,2,3])输出s0中的元素；放在②处，则按照正常顺序输出，符合人们
的思维习惯。
放在①处，执行顺序符合人们的思维习惯，但输出结果却不同，为何呢？
原因为：放在①处，执行到[1,2,3]处时，又打开了一个文件，上一个打开的文件还没有关闭，
[1,2,3]执行完后，才关闭其打开的文件，再关闭s0打开的文件，这样就会出现上述所说的
输出结果；放在②处，每次执行一个条件语句就关闭一次文件，这样可以及时的保存文件。
'''

#递归函数
def list_ch(lis_1):
    print lis_1
    
    #f2 = open('test_1.txt','w') #①
    i = 0
    while i <= len(lis_1) - 1:
        
        f2 = open('test_1.txt','a') #②
        
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
  
#利用递归函数实现list中的list元素中的项按照同样格式输出
