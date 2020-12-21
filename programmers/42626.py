# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 06:29:06 2020

@author: EVer
"""

def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        if len(scoville) == 1:
            return -1
        a = scoville.pop(scoville.index(min(scoville)))
        b = scoville.pop(scoville.index(min(scoville)))
        n = a + (b * 2)
        print(n)
        scoville.append(n)
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 1000
print(solution(scoville, K))