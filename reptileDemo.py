#-*-coding:utf-8-*-

#����while���ʵ��ˢ΢�������͹ر������������

#��ε��÷�Ĭ�ϵ��������������

'''
����ʹ������taskkill /F /IM chrome.exe���ر����������������windows����
'''
import webbrowser as web
import time
import os
import random

j = 0
r = random.randint(2,4) #����һ����СΪ2�����Ϊ4������
while j < r:
    i = 0
    while i <= 9:
        web.open_new_tab('https://www.baidu.com/') #�˱�ǩʹ��Ĭ���������
        i = i + 1
        time.sleep(0.8)  #����ҳʱ�ĵȴ�ʱ��(��λ�ǣ���)
    else:
        os.system('taskkill /F /IM chrome.exe')
        print j,'times closing webbrowser !'
    j = j + 1