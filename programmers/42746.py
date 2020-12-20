# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 03:37:14 2020

@author: EVer
"""
def solution(numbers):
    
    answer = ''
    number_str = list(map(str, numbers))
    sorted_number = sorted(number_str, key=lambda x: (x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse=True)
    for i in sorted_number:
        answer += i
    if int(answer) == 0:
        answer = '0'
    return answer
   
numbers = [3, 30, 34, 5, 9]
solution(numbers)
