#!/usr/bin/python

import socket
import sys

file_object = open('list.txt', 'r')
#line = file_object.readline()

#for i in input:
for line in file_object.readlines():
	values = line.split()

	if len(values) > 2:
		print "Below 2 Characters or None"
	else:
	
		print "Usage: vrfy.py <username>"
		print line
		
	# Create a Socket
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to a server
	
		connect=s.connect(('192.168.15.237',25))

	# Receive the banner

		banner=s.recv(1024)

		print banner

	# VRFY a user

		s.send('VRFY ' + line  + '\r\n')

		result=s.recv(1024)

		print result
#		print "hi"
	# Close the socket

		s.close()
