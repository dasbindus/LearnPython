#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 在Windows下失败，由于Windows没有进程树的概念，创建出来的进程是独立的

from multiprocessing import Process, Queue
import os, time, random


#写数据进程执行的代码
def write(q):
	for value in ['A', 'B', 'C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())

#读数据进程的代码
def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue...' % value

if __name__ == '__main__':
	#父进程创建Queue，并传给各个子进程
	q = Queue()
	pw = Process(target = write, args = (q, ))
	pr = Process(target = read, args = (q, ))
	# 启动子进程pw，写入
	pw.start()
	# 启动子进程pr，读取
	pr.start()
	# 等待pw结束
	pw.join() # join()作用：等待一个进程/线程终止
	# pr进程中为死循环，需要强行结束
	pr.terminate()