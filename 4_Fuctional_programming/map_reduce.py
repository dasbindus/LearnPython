#! /usr/bin/env python

print map(str, [1,2,3,4,5,6])

print '----------------dividing line---------------------'

# using reduce() to change [1,3,5,7,9] to 13579
def fn(x, y):
	return x * 10 + y
print reduce(fn, [1,3,5,7,9])

print '----------------dividing line---------------------'

# using former to achieve str2int {it's int() actually}
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }[s]
	return reduce(fn, map(char2num, s))
print str2int('0123456789'), '\n', int('0123456789')

print '----------------practice 1-------------------'
# input ['adam', 'LISA', 'barT']
# output ['Adam', 'Lisa', 'Bart']
def onlyFirstUpper(s):
	return map(lambda x: x[0].upper() + x[1:].lower(), s)
print onlyFirstUpper(['adam', 'LISA', 'barT'])

print '----------------practice 2--------------------'
# param is a list ,output is product
def prod(L):
	return reduce(lambda x, y: x * y, L)
print prod([1, 2, 3, 4, 5, 6, 7, 8, 9])
	