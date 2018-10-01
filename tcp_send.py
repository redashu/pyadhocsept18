#!/usr/bin/python2

import  socket,time

#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket.socket()  # by default tcp socket will be created with ipv4

#  now i am connecting 
s.connect(("192.168.10.127",7789))
while True:
	s.send("Hello world")
	time.sleep(1)
	print s.recv(10)



s.close()


