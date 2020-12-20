# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 05:53:32 2020

@author: EVer
"""

def solution(tickets):
    t = {}
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]
            
    for k in t.keys():
        t[k] = sorted(t[k], reverse=True)
        
    start = ["ICN"]
    answer = []
    
    while start:
        curr = start[-1]
        
        if curr not in t or len(t[curr]) == 0:
            answer.append(start.pop())
        else:
            start.append(t[curr].pop())
    answer.reverse()
    return answer

tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(tickets))