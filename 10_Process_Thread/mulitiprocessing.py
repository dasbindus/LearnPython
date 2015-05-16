#! /usr/bin/env python
#Filename: multiprocessing.py

from multiprocessing import Process
import os


# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid  == 0:
# 	print 'child process (%s), parent is (%s).' % (os.getpid(), os.getppid())
# else:
# 	print 'parent process (%s), child is (%s).' % (os.getpid(), pid)

def run_proc(name):
	print 'run child process %s (%s)' % (name, os.getpid())	

if __name__ == '__main__':
	print 'Parent process %s' % os.getpid()
	p = Process(target = run_proc, args = ('test',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end.'