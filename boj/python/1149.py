# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:19:35 2021

"""

if __name__=="__main__":
    n = int(input())
    grid = []
    price = float('inf')

    for _ in range(n):
        grid.append(list(map(int, input().split())))

    for i in range(1, n):
        grid[i][0] = min(grid[i-1][1], grid[i-1][2]) + grid[i][0]
        grid[i][1] = min(grid[i-1][0], grid[i-1][2]) + grid[i][1]
        grid[i][2] = min(grid[i-1][0], grid[i-1][1]) + grid[i][2]
    print(min(grid[-1]))

"""
처음에 어떻게 값을 갱신해야 하나 싶었는데 이전 값 중 작은 값을 현재 값에 더하여 갱신하는 방법으로 문제를 해결하였다.
"""