# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 05:05:51 2020

@author: EVer
"""

def install_station(s, w, n, installed):
    installed[s] = 1
    if s + w <= n:
        max_w = s + w
    else:
        max_w = n
    if s - w >= 1:
        min_w = s - w
    else:
        min_w = 1
    # len_s = max_w - min_w
    # installed[min_w:max_w] = [1] * len_s
    # installed[max_w] = 1
    for i in range(min_w, max_w + 1):
        installed[i] = 1
    # for i in range(1, w + 1):
    #     if s + i <= n:
    #         installed[s + i] = 1
    #     if s - i >= 1:
    #         installed[s - i] = 1

def solution(n, stations, w):
    answer = 0
    zero_index = 1
    installed = [0] * (n + 1)
    installed[0] = 1
    for s in stations:
        install_station(s, w, n, installed)
    while 0 in installed:
        block = 0
        while installed[zero_index] != 0:
            zero_index += 1
        s = zero_index
        for i in range((w * 2) + 1):
            if s + i <= n and installed[s + i] == 0:
                block += 1
            else:
                break
        s += block // 2
        install_station(s, w, n, installed)
        answer += 1
    return answer

n = 10000
stations = []
w = 1
print(solution(n, stations, w))