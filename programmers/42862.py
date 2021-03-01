# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 03:02:48 2021

"""

def solution(n, lost, reserve):
    answer = n - len(lost)
    dp = [0] * n
    for i in reserve:
        dp[i - 1] = 1
    for i in lost[:]:
        if dp[i - 1] == 1:
            answer += 1
            dp[i - 1] = 0
            lost.remove(i)
    for i in lost:
        if i == 1:
            if dp[i] == 1:
                answer += 1
                dp[i] = 0
        elif i == n:
            if dp[i - 2] == 1:
                answer += 1
                dp[i - 2] = 0
        else:
            if dp[i - 2] == 1:
                answer += 1
                dp[i - 2] = 0
            elif dp[i] == 1:
                answer += 1
                dp[i] = 0
    return answer

n = 5
lost = [1, 2, 3]
reserve = [2, 3, 4]
ret = solution(n, lost, reserve)
print(ret)
