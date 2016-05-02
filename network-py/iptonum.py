#!/usr/bin/env python 

import socket
from binascii import hexlify

def ip_num():
    remote_name = 'www.baidu.com'

    ip_baidu = socket.gethostbyname(remote_name)
    print 'baidu_ip: %s' %ip_baidu
    ip_add = ['127.0.0.1','10.0.0.1']

    for i in ip_add:
        pack_ip = socket.inet_aton(i)
        unpack_ip = socket.inet_ntoa(pack_ip)
        print 'ip_add: %s =>num:%s =>unpack_num:%s' %(i,pack_ip,unpack_ip)
        print 'hex_ip: %s' %hexlify(pack_ip)


if __name__ == '__main__':
    ip_num()
