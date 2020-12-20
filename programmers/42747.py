# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 04:39:10 2020

@author: EVer
"""

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for n, c in enumerate(citations):
        if c >= (n + 1):
            answer += 1
    return answer

citations = [10, 9, 4, 1, 1]
print(solution(citations))