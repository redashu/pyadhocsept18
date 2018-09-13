#!/usr/bin/env python2

import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.10.201"
port=7890

while  True :
#  sending  data to  target machine 
	cmd=raw_input("enter your command :   ")
	s.sendto(cmd,(ip,port))













