# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:15:53 2020

@author: EVer
"""

def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                print(phone_book[j].find(phone_book[i]))
                return False
    answer = True
    return answer

phone_book = ['123', '456', '789']
print(solution(phone_book))