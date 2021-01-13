# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 02:31:09 2020

@author: EVer
"""

def solution(priorities, location):
    answer = 0
    while True:
        if max(priorities) == priorities[0]:
            priorities.pop(0)
            answer += 1
            if location == 0:
                break;
            elif location != 0:
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0