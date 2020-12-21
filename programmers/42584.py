# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:53:19 2020

@author: EVer
"""

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            print(prices[i], prices[j])
            if prices[i] > prices[j]:
                answer[i] += 1
                break;
            else:
                answer[i] += 1
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))