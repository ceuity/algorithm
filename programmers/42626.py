# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 06:29:06 2020

@author: EVer
"""

from heapq import heappop, heappush

def solution(scoville, K):
    scoville.sort()
    answer = 0
    while True:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + (b * 2))
        answer += 1
        k = heappop(scoville)
        if k >= K:
            return answer
        else:
            heappush(scoville, k)
        if len(scoville) < 2:
            return -1

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))