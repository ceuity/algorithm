# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 02:03:49 2021

"""

from collections import deque

if __name__ == '__main__':
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input())))
    count = 1
    next_q = deque([[0, 0]])
    
    def find_maze(i, j):
        if i >= 0 and i < h and j >= 0 and j < w:
            if grid[i][j] == 1:
                return [i, j]
    q = next_q.copy()
    while q:
        curr = q.popleft()
        y, x = curr
        if x == w - 1 and y == h - 1:
            print(count)
            break
        else:
            if grid[y][x] == 1:
                grid[y][x] = 0

                if find_maze(y+1, x):
                    next_q.append(find_maze(y+1, x))
                if find_maze(y-1, x):
                    next_q.append(find_maze(y-1, x))
                if find_maze(y, x+1):
                    next_q.append(find_maze(y, x+1))
                if find_maze(y, x-1):
                    next_q.append(find_maze(y, x-1))
        if not q:
            count += 1
            q = next_q.copy()
            
"""
DFS인줄 알고 풀었는데 답이 이상해서 확인해보니 BFS로 푸는 문제였다...
각 위치에서 queue에 담은 좌표들을 모두 방문해야 한 사이클이 끝난 것으로 봐야 한다.
"""