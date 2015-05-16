#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def getName(self):
		return self.__name

	def getScore(self):
		return self.__score

	def setNameScore(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)

jack = Student('Jack Bai', 98)
# print jack.name, jack.score
jack.print_score()
jack.setNameScore('Chenlina', 90)
jack.print_score()

jack.age = 24
print jack.age