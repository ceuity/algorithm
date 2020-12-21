# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:43:58 2020

@author: EVer
"""

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_counts = len(truck_weights)
    bridge = [0] * bridge_length
    truck_passed = []
    while truck_weights or len(truck_passed) != truck_counts:
        if truck_weights and sum(bridge) + truck_weights[0] - bridge[0] <= weight:
            if bridge[0] == 0:
                bridge.pop(0)
            else:
                truck_passed.append(bridge.pop(0))
            bridge.append(truck_weights.pop(0))
        else:
            if bridge[0] == 0:
                bridge.pop(0)
            else:
                truck_passed.append(bridge.pop(0))
            bridge.append(0)
        answer += 1
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
