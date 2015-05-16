#! /usr/bin/env python
#Filename: property.py
# -*- coding:utf-8 -*-

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score has to be an Integer.')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100.')
		self._score = value

	@property
	def age(self):
		self._age = 23
		return self._age

s = Student()
s.score = 90
# s.age = 123 #can't set age; age is read only
print s.age
print s.score