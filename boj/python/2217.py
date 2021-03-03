# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:16:50 2021

"""

if __name__ == "__main__":
    n = int(input())
    if n == 0:
        print ('0')
        exit
    ropes = []
    temp = []
    answer = 0
    for _ in range(n):
        ropes.append(int(input()))
    ropes.sort(reverse=True)
    for rope in ropes:
        temp.append(rope)
        if temp[-1] * len(temp) > answer:
            answer = temp[-1] * len(temp)
    print(answer)