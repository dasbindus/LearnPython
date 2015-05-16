#! /usr/bin/env python
# Filename: tcpServer.py

import socket, time, threading

def tcplink(sock, addr):
	print 'addr is :' , addr
	print 'Accept new connection from %s:%s...' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s!' % data)
	sock.close()
	print 'connection from %s:%s closed.' % addr

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
s.bind(('10.12.134.125', 9999))

# listen
s.listen(5)
print 'Waiting for connection'

while True:
	# accept a connection
	sock, addr = s.accept()
	# use thread to handle the tcp connection
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()