#! /usr/bin/env python
# -*- coding:utf-8 -*-

def age_test():
	age = int(raw_input('your age is:'))
	if age >= 18:
		print 'You are a adult.\n'
	elif age >= 12:
		print 'You are a teenager.\n'
	else:
		print 'You are a kid.'


def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)


# -------------------------------
# age_test();

print fact(10)