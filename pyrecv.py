#!/usr/bin/env python2

import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.10.217"
port=7890
#  binind ip and port with bind function that takes input as tuple
s.bind((ip,port))

while 5 > 2 :
#  now receiving data
	print   s.recvfrom(100)





















