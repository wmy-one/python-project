#-*-coding:utf-8-*-

#本程序实现调用第三方模块的功能
'''
首先载入第三方模块，可以通过help(module_name)查看模块的中包含的方法
再通过module_name.method(parameters)来实现模块的函数的调用
'''

import urllib
import webbrowser
#import webbrowser as web  
#给webbrwser设置类型别名为web，通过web便可以调用webbrowse模块的相关功能

url = "http://www.baidu.com"
content = urllib.urlopen(url).read()

#以可写的方式打开一个文件‘baidu.com.html’，调用write()方法将其中的参数写到文件中
open('baidu.html','w').write(content)
webbrowser.open_new_tab('baidu.com.html')
#web.open_new_tag('baidu.com.html')