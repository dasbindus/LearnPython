#! /usr/bin/env python
# filter.py

def is_odd(n):
	return n % 2 == 1
print filter(is_odd, [1,2,3,4,5,6,7,8,9,0])

def not_empty(s):
	return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, '', 'C', ''])

print '------------------practice-------------------'

print filter(lambda x: [x % i for i in range(2, x) if x % i == 0],range(1,101))