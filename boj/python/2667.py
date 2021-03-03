# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:12:46 2021

"""

from collections import defaultdict

if __name__ == "__main__":
   
    n = int(input())
    grid = []
    answer = 0
    house = defaultdict(int)

    def dfs(i, j, index):
        if i >= 0 and i < n and j >= 0 and j < n:
            if grid[i][j] == 1:
                grid[i][j] = 0
                house[index] += 1
        
                dfs(i+1, j, index)
                dfs(i-1, j, index)
                dfs(i, j+1, index)
                dfs(i, j-1, index)
    
    for _ in range(n):
        grid.append(list(map(int, input())))
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, answer + 1)
                answer += 1
    print(answer)
    house = sorted(house.items(), key=lambda x:x[1])
    for key, value in house:
        print(value)
        
"""
정석적인 dfs 문제인 것 같다. grid를 전부 탐색하여 나누어진 땅 마다 index를 부여하여 dict에 기록하였다.
"""