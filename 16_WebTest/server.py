#! /usr/bin/env python
# server.py

from wsgiref.simple_server import make_server
from hello import application


# create a server, IP is empty, port is 9999, handle func is 'application'
httpd = make_server('10.12.134.125', 9999, application)
print 'Server HTTP on Port 9999 ...'

# start listen Http request
httpd.serve_forever()