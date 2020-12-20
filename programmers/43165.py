# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:29:59 2020

@author: EVer
"""

answer = 0

def recursive(numbers, target, temp):
    global answer
    if len(numbers) == 0:
        if temp == target:
            answer += 1
        return
    for i in range(2):
        if i % 2 == 0:
            temp_pos = temp + numbers[0]
            recursive(numbers[1:], target, temp_pos)
        else:
            temp_neg = temp + (numbers[0] * -1)
            recursive(numbers[1:], target, temp_neg)
    return

def solution(numbers, target):
    recursive(numbers, target, 0)
    return answer