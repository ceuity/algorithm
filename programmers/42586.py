# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:05:13 2020

@author: EVer
"""

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    remain_time = deque()
    for i in range(len(progresses)):
        remain_time.append(math.ceil((100 - progresses[i]) / speeds[i]))
    while remain_time:
        ret = 1
        finish = remain_time.popleft()
        while remain_time and finish >= remain_time[0]:
            remain_time.popleft()
            ret += 1
        answer.append(ret)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))