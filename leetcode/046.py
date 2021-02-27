# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 03:10:20 2021

@author: EVer
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                ans.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        return ans
        
nums = [1, 2, 3]
ret = Solution()
print(ret.permute(nums))