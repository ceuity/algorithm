# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 02:56:47 2020

@author: EVer
"""

def solution(clothes):
    answer = 1
    wear_type = []
    for wear in clothes:
        if wear[1] not in wear_type:
            wear_type.append(wear[1])
    for i in wear_type:
        sums = 0
        for cloth in clothes:
            if cloth[1] == i:
                sums += 1
        answer *= (sums + 1)
    return (answer - 1)

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
