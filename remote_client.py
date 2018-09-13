#!/usr/bin/env python2

import  socket,commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.10.198"
port=7890

# defining list for 10 commands counter
timer=[]
while  True :
#  sending  data to  target machine 
	cmd=raw_input("[root@station254 ~]# ")
	s.sendto(cmd,(ip,port))
	if  'exit' in  cmd  or  'close' in cmd:
		print "closing server.."
		exit()
	else :
		timer.append(cmd)
		print len(timer)
		if  len(timer) > 5 :
			print commands.getoutput('clear')
			print  timer
			for i in  range(len(timer)):
				timer.pop()
		else :
			pass

s.close()


