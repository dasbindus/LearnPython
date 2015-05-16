#! /usr/bin/env python

import os


print os.name
print os.uname()
print os.environ
print os.getenv('PATH'), '\n'


print os.path.split('/home/baidong/workspaces/python/fileTest/hello.txt')
print os.path.splitext('/home/baidong/workspaces/python/fileTest/hello.txt')
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print '\n', os.path.abspath('.')
if os.path.exists(os.path.join('/home/baidong/workspaces/python/fileTest','testDir')):
	os.rmdir('/home/baidong/workspaces/python/fileTest/testDir')
print [x for x in os.listdir('.') if os.path.isdir(x)]
os.mkdir('/home/baidong/workspaces/python/fileTest/testDir')
print [x for x in os.listdir('.') if os.path.isdir(x)]