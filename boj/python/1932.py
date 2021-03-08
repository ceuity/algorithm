# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:33:01 2021

"""

if __name__=="__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(len(grid[i])):
            if j == 0:
                grid[i][j] = grid[i][j] + grid[i-1][j]
            elif j == len(grid[i]) - 1:
                grid[i][j] = grid[i][j] + grid[i-1][j-1]
            else:
                grid[i][j] = grid[i][j] + max(grid[i-1][j-1], grid[i-1][j])
    print(max(grid[-1]))
"""
1149와 비슷한 유형의 문제.
현재 위치에서 이전 값을 더하여 갱신하면서 다음으로 넘어간다.
"""