#!/usr/bin/env python

import socket

def hostInfo():

    host_name = socket.gethostname()
    print 'host_name: %s' %host_name

    host_IP = socket.gethostbyname(host_name)
    print 'host_IP: %s' %host_IP

    print "****your host information is:****"
    print '-'*33
    print '***| host_name |***| host_IP |***'
    print '***|%11s|***|%s|***' %(host_name,host_IP)
    print '-'*33

if __name__ =='__main__':
    hostInfo()
