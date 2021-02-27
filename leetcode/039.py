# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 01:59:59 2021

"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                ans.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        dfs(target, 0, [])
        return ans

        
candidates = [2,3,6,7]
target = 7
ret = Solution()
print(ret.combinationSum(candidates, target))