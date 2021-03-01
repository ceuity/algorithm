# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 05:07:52 2021

"""

def solution(number, k):
    i = 0
    while k > 0:
        if number[i] < number[i+1]:
            number = number[:i] + number[i+1:]
            k -= 1
            if i > 0:
                i -= 1
        elif i < len(number) - 2:
            i += 1
        else:
            number = number[:-k]
            k = 0
    answer = number
    return answer

number = "999"
k = 1
ret = solution(number, k)
print(ret)