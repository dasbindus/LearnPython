#! /usr/bin/env python
# Filename: tcpClient.py

import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
s.connect(('10.12.134.125', 9999))
# receive data
print s.recv(1024)
for data in ['baidong', 'chenlina', 'baizhen']:
	# send data
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()