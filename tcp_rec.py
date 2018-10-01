#!/usr/bin/python2

import  socket

#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s=socket.socket()  # by default tcp socket will be created with ipv4
#  now binding with all current ip and one port 
s.bind(("",7789))
# listen function for concurrent connection
s.listen(5) # that means 5 connections at a single point of time


while True:
	clisock,cliaddr=s.accept()  #  this receive data from  s.connect 
	data=clisock.recv(100)
	clisock.send('okey got it')


s.close()

