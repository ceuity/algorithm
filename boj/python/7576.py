# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:13:24 2021

"""

from collections import deque

if __name__ == '__main__':
    m, n = map(int, input().split())
    count = 0
    grid = []
    q = deque([])
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    def check_grid(i, j):
        if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 0:
            return [i, j]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append([i, j])
    temp = deque([])
    while q:
        curr = q.popleft()
        i, j = curr
        if check_grid(i+1, j):
            grid[i+1][j] = 1
            temp.append([i+1, j])
        if check_grid(i-1, j):
            grid[i-1][j] = 1
            temp.append([i-1, j])
        if check_grid(i, j+1):
            grid[i][j+1] = 1
            temp.append([i, j+1])
        if check_grid(i, j-1):
            grid[i][j-1] = 1
            temp.append([i, j-1])
        if not q:
            q = temp.copy()
            temp = deque([])
            count += 1

    # 익지 않은 토마토가 있을 경우
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                count = 0
                break
    print(count-1)

"""
일반적인 bfs 문제와는 달리 q에 해당 토마토 주변의 익지 않은 토마토를 넣어주어야 한다.
"""