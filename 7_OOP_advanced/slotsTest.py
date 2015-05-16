#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: slotsTest.py

class Student(object):
	# __slots__ is used to limit the attributes
	__slots__ = ('name', 'age')
	def __init__(self, name, age):
		self.name = name
		self.age = age

me = Student('baidong', 23)
print me.age