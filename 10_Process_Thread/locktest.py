#! /usr/bin/env python

import time, threading

# my bank balance
balance = 0
# use lock to make sure there are only one thread changing balance
lock = threading.Lock()

def change_balance(n):
	# check_in then check_out, balance remains 0
	global balance
	balance += n
	balance -= n

def run_thread(n):
	for i in range(100000):
		# get a lock first
		lock.acquire()
		try:
			change_balance(n)
		finally:
			# release lock
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5, ))
t2 = threading.Thread(target = run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print balance