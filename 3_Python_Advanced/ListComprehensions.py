#! /usr/bin/env python

L = []
for x in range(1,11):
	L.append(x*x)
print L

L = [x * x for x in range(1,11)]
print L

L = [x * x for x in range(1,11) if x % 2 ==0]
print L

L = [m + n for m in 'ABC' for n in 'XYZ']
print L

import os
L = [d for d in os.listdir('.')]
print L

L = ['HellO', 'IBM', 'TEsT', 'AcaDFIJxDADc']
print [s.lower() for s in L]

x = 12,
y = 'asd'
print isinstance(x,str)
print isinstance(y,str)
