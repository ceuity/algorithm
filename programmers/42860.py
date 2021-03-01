# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 03:33:32 2021

"""

def solution(name):
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    index = 0
    answer = 0
    
    while True:
        answer += change[index]
        change[index] = 0
        if sum(change) == 0:
            return answer
        
        left = 1
        right = 1
        while change[index - left] == 0:
            left += 1
        while change[index + right] == 0:
            right += 1
        answer += left if left < right else right
        index += -left if left < right else right

name = "BBBAAAB"
ret = solution(name)
print(ret)