#-*-coding:utf-8-*-

#������ʵ�ֵ��õ�����ģ��Ĺ���
'''
�������������ģ�飬����ͨ��help(module_name)�鿴ģ����а����ķ���
��ͨ��module_name.method(parameters)��ʵ��ģ��ĺ����ĵ���
'''

import urllib
import webbrowser
#import webbrowser as web  
#��webbrwser�������ͱ���Ϊweb��ͨ��web����Ե���webbrowseģ�����ع���

url = "http://www.baidu.com"
content = urllib.urlopen(url).read()

#�Կ�д�ķ�ʽ��һ���ļ���baidu.com.html��������write()���������еĲ���д���ļ���
open('baidu.html','w').write(content)
webbrowser.open_new_tab('baidu.com.html')
#web.open_new_tag('baidu.com.html')