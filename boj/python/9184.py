# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:14:51 2021

"""

if __name__ == '__main__':
	dict = {}
	dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

	def w(a, b, c):
		num = ' '.join(map(str, [a, b, c]))
		if a <= 0 or b <= 0 or c <= 0:
			if num not in dict:
				dict[num] = 1
			return dict[num]
		elif a > 20 or b > 20 or c > 20:
			if num not in dict:
				dict[num] = w(20, 20, 20)
			return dict[num]
		elif a < b and b < c:
			if num not in dict:
				dict[num] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
			return dict[num]
		else:
			if num not in dict:
				dict[num] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
			return dict[num]



	while True:
		a, b, c = map(int, input().split())
		if a == b == c == -1:
			break
		print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


	# def w2(a, b, c):
	#
	# 	# dp 테이블에 이미 연산되어 저장된 값이 있다면, 그 값을 리턴
	# 	if dp[a + 50][b + 50][c + 50] != 0:
	# 		return dp[a + 50][b + 50][c + 50]
	#
	# 	# 조건에 맞춰 연산을 수행한 후, 그 결과값을 dp 테이블에 저장 후 리턴
	# 	if a <= 0 or b <= 0 or c <= 0:
	# 		dp[a + 50][b + 50][c + 50] = 1
	# 		return 1
	# 	if a > 20 or b > 20 or c > 20:
	# 		temp = w2(20, 20, 20)
	# 		dp[a + 50][b + 50][c + 50] = temp
	# 		return temp
	# 	if a < b and b < c:
	# 		temp = w2(a, b, c - 1) + w2(a, b - 1, c - 1) - w2(a, b - 1, c)
	# 		dp[a + 50][b + 50][c + 50] = temp
	# 		return temp
	# 	else:
	# 		temp = w2(a - 1, b, c) + w2(a - 1, b - 1, c) + w2(a - 1, b, c - 1) - w2(a - 1, b - 1, c - 1)
	# 		dp[a + 50][b + 50][c + 50] = temp
	# 		return temp

"""
a, b, c를 str로 변경하여 딕셔너리에 넣는 방법으로 했더니 오답으로 처리되어서 다시 생각해보니 
11 2 2 나 1 1 22와 같은 숫자가 같은 값으로 처리된다는 것을 깨달았다. 이것을 공백으로 구분하여 11 2 2와 1 1 22가 다른 것으로 인식되게 했다. 
"""