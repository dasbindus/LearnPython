#! /usr/bin/env python

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
 
@log('execute')
def now():
	print '2015-4-9'

now()