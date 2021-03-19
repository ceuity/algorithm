# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:05:11 2021

"""

if __name__=='__main__':
	string = str(input())

	def longestPalindrome(s):
		if len(s) == 1 or s == s[::-1]:
			return s
		start_index = 1
		maxlen = 1
		for i in range(1, len(s)):
			odd = s[i - maxlen - 1: i + 1]
			even = s[i - maxlen: i + 1]
			if i - maxlen - 1 >= 0 and odd == odd[::-1]:
				start_index = i - maxlen - 1
				maxlen += 2
			elif i - maxlen >= 0 and even == even[::-1]:
				start_index = i - maxlen
				maxlen += 1
		return s[start_index:start_index + maxlen]

	print(len(longestPalindrome(string)))

"""
이전에 leetcode에서 풀었던 가장 긴 팰린드롬 문자열 문제랑 같지만 거기서는 브루트 포스를 이용해 풀었기 때문에
그대로 풀었더니 시간 초과가 났다. 따라서 O(N)으로 풀이하였다.
"""