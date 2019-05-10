# -*- coding: utf-8 -*-
"""
Test of UDP client code
Created on Mon May  6 20:40:46 2019

@author: swedd
"""

import socket

UDP_IP_ADDRESS = "192.168.0.20"
UDP_PORT_NO = 6789
Message = "Hello, Server"
print("test")

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))