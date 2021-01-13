# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 00:26:48 2020

@author: EVer
"""

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [0]
    for i in range(1, len(prices)):
        for j in range(i):
            if prices[i] < prices[i - j - 1]:
                answer[i - j - 1] = i - stack.pop()
            else:
                break;
        stack.append(i)
    final_time = stack[-1]
    for t in stack:
        answer[t] = final_time - t
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))