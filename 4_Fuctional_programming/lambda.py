#! /usr/bin/env python

f = lambda x: x * x
print f, f(4)

print map(lambda x: x * x, range(1,10))