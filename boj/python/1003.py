# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:01:09 2021

"""

if __name__ == '__main__':
	n = int(input())
	dict = {}

	def fibonacci(n):
		if n == 0:
			if 0 not in dict:
				dict[0] = [1, 0]
			return dict[0]
		elif n == 1:
			if 1 not in dict:
				dict[1] = [0, 1]
			return dict[1]
		else:
			if n not in dict:
				dict[n] = [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]]
			return dict[n]

	for i in range(n):
		print(" ".join(map(str, fibonacci(int(input())))))

"""
피보나치 함수의 딕셔너리를 만들어서 각 n값에 0과 1의 list를 저장하도록 했다.
"""