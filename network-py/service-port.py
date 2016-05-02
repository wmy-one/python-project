#!/usr/bin/env python

import socket

def port_service():
    port = [25,80]

    for i in port:
        serv_port = socket.getservbyport(i,'tcp')
        print 'port: %s => serv_port: %s' %(i,serv_port)

    print 'port: %s => serv_port_tcp: %s => serv_port_udp:%s' %('53',socket.getservbyport(53,'tcp'),socket.getservbyport(53,'udp'))

if __name__ == '__main__':
    port_service()
