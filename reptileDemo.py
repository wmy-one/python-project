#-*-coding:utf-8-*-

#利用while语句实现刷微博次数和关闭浏览器的爬虫

#如何调用非默认的浏览器？？？？

'''
可以使用命令taskkill /F /IM chrome.exe来关闭浏览器，此命令是windows命令
'''
import webbrowser as web
import time
import os
import random

j = 0
r = random.randint(2,4) #产生一个最小为2，最大为4的整数
while j < r:
    i = 0
    while i <= 9:
        web.open_new_tab('https://www.baidu.com/') #此标签使用默认浏览器打开
        i = i + 1
        time.sleep(0.8)  #打开网页时的等待时间(单位是：秒)
    else:
        os.system('taskkill /F /IM chrome.exe')
        print j,'times closing webbrowser !'
    j = j + 1