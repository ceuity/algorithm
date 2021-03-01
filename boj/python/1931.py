# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:43:10 2021

"""

if __name__ == '__main__':
    n = int(input())
    meetings = []
    count = 0
    end = 0
    for _ in range(n):
        meetings.append(list(map(int, input().split())))
    meetings.sort(key=lambda x:(x[1], x[0]))
    for o, c in meetings:
        if end <= o:
            count += 1
            end = c
    print(count)