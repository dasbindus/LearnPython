#! /usr/bin/env python

# generator -- list
g = (x * x for x in range(1,11))
for i in g:
	print i


print '-----------------slice--------------------'
# generator -- fuc(using yield)
# Fibonacci
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n += 1

for i in fib(8):
	print i