# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 00:53:28 2021

"""

import sys
from collections import deque
import copy
sys.setrecursionlimit(100000)

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    grid = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    q = deque()

    def dfs(y, x, num):
        if 0 <= x < n and 0 <= y < n and visited[y][x] == 0:
            if grid[y][x] == 1:
                visited[y][x] = 1
                grid[y][x] = num
                dfs(y+1, x, num)
                dfs(y-1, x, num)
                dfs(y, x+1, num)
                dfs(y, x-1, num)
            elif grid[y][x] == 0:
                q.append([y, x, num])

    nums = 2
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if grid[i][j] == 1:
                    dfs(i, j, nums)
                    nums += 1
                else:
                    visited[i][j] = 1
    answer = []
    def bfs(y, x, num, grid_copy):
        dq = deque([[y, x]])
        dist = 0
        while dq:
            for _ in range(len(dq)):
                _y, _x = dq.popleft()
                if 0 <= _y < n and 0 <= _x < n:
                    if grid_copy[_y][_x] == 0:
                        grid_copy[_y][_x] = num
                        dq.append([_y+1, _x])
                        dq.append([_y-1, _x])
                        dq.append([_y, _x+1])
                        dq.append([_y, _x-1])
                    elif grid_copy[_y][_x] != num:
                        return dist
            dist += 1
        return (float('inf'))
    while q:
        y, x, num = q.popleft()
        answer.append(bfs(y, x, num, copy.deepcopy(grid)))
    print(min(answer))

"""
탐색을 두 번 해야 하는 문제였다. 먼저 섬을 Grouping 해준 다음 섬의 끝 지점에서 BFS로 인접한 섬 까지의 거리를 구하였다.
"""