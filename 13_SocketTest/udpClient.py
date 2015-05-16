O#! /usr/bin/env python
# Filename: udpClient.py

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['baidong', 'chenlina', 'baizhen']:
	# send data
	s.sendto(data, ('10.12.134.125',9998))
	# receive data
	print s.recv(1024)
s.close()