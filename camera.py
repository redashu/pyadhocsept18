#!/usr/bin/python3

import cv2

#  we are using  camera first 
cap=cv2.VideoCapture(0)

while cap.isOpened() :
	status,frame=cap.read()
	cv2.line(frame,(0,0),(100,100),(0,0,255),3)
	cv2.rectangle(frame,(20,20),(200,200),(123,5,34),3)
	# circle and text , 
	#cv2.line(frame,(30,40),(300,200),(100,43,255),5)
	cv2.imshow('live',frame)
	if cv2.waitKey(10)  &  0xFF  == ord('a'):
		break


cv2.destroyAllWindows()
cap.release()




