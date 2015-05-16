#! /usr/bin/env python


######################## Read File ##############################
# use try...finally..
try:
	f = open('/home/baidong/workspaces/python/fileTest/hello.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()

# or use with...as...
with open('/home/baidong/workspaces/python/fileTest/hello.txt', 'r') as f:
	print f.read()

# open a pic
# f1 = open('/home/baidong/workspaces/python/fileTest/test.jpg', 'rb')
# print f1.read()

######################### Write File ########################
with open('/home/baidong/workspaces/python/fileTest/hello.txt', 'w') as f:
	f.write('hello world!!!!')