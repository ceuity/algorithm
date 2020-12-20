# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 04:32:38 2020

@author: EVer
"""

from operator import itemgetter

def check_next(city, tickets):
    for ticket in tickets:
        if city[1] == ticket[0]:
            return True
    return False

def solution(tickets):
    tickets = sorted(tickets, key=itemgetter(0, 1))
    answer = []
    start = "ICN"
    queue = [start]
    while queue:
        start = queue.pop()
        if len(tickets) == 0:
            answer.append(start)
            return answer
        for city in tickets:
            if start == city[0] and check_next(city, tickets):
                answer.append(city[0])
                queue.append(city[1])
                tickets.remove(city)
            elif len(tickets) == 1:
                answer.append(city[0])
                queue.append(city[1])
                tickets.remove(city)
    return answer

# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
tickets = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(tickets)
print(solution(tickets))

