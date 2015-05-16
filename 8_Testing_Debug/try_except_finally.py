#! /usr/bin/env python
import logging

# logging
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)

main()


# try_except_finally
try:
	print 'try...'
	r = 10/0
	print 'result:', r
except ZeroDivisionError, e:
	print 'except:', e
else:
	pass
finally:
	print 'finally'
print 'END'