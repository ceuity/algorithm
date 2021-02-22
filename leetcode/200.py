# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:09:18 2021

"""
from typing import List

class Solution:
    def dfs(self, i: int, j: int, grid: List[List[str]]):
        if i < 0 \
        or i >= len(grid) \
        or j < 0 \
        or j >= len(grid[0]) \
        or grid[i][j] != '1':
            return
        
        grid[i][j] = '0'
        # 동서남북 탐색
        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    ans += 1
        return ans
        
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

ret = Solution()
print(ret.numIslands(grid))