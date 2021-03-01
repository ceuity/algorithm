# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:32:41 2021

"""

if __name__ == '__main__':
    n, k = map(int, input().split())
    moneys = []
    for _ in range(n):
        moneys.append(int(input()))
    moneys.reverse()
    count = 0
    for money in moneys:
        count += k // money
        k = k % money
    print(count)