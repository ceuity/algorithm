# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:58:46 2021

"""

if __name__ == '__main__':
	# n = int(input())
	# count = 0
	# total = 1
	# for i in range(0, n):
	# 	count += i % 2
	# 	total += count
	# print(total % 15746)

	n = int(input())
	a, b = 0, 1
	for i in range(n):
		a, b = b % 15746, (a + b) % 15746
	print(b)
"""
피보나치
"""