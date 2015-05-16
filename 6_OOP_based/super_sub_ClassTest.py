#! /usr/bin/env python
# -*- coding:utf-8 -*-
# -------继承和多态--------
class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print 'dog is running...'
	def eat(self):
		print 'eating meal...'

class Cat(Animal):
	def run(self):
		print 'cat is running'

dog = Dog()
dog.run()
cat = Cat()
cat.run()

print isinstance(cat, Animal)
print type(dog)
print dir(dog)