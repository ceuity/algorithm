# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:29:19 2020

@author: EVer
"""

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for comp in completion:
        temp -= int(hash(comp))
    return dic[temp]
    
participant = ['leo', 'kiki', 'eden']
completion = ['kiki', 'eden']

solution(participant, completion)