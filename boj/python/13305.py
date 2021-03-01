# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 02:20:31 2021

"""

if __name__ == "__main__":
    n = int(input())
    dist = list(map(int, input().split()))
    cities = list(map(int, input().split()))
    ans = 0
    length = 0
    price = cities[0]
    for i in range(len(cities)):
        if i == len(cities) - 1:
            ans += length * price
        elif cities[i] < price:
            ans += length * price
            price = cities[i]
            length = dist.pop(0)
        else:
            length += dist.pop(0)
    print(ans)