# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 01:21:34 2021

"""

from typing import List

# 676ms
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        ans = []
        def dfs(m: int, n: int, k: int, stack: List, ans: List):
            for i in range(m, n + 1):
                if i not in stack:
                    stack.append(i)
                    if len(stack) == k:
                        print(stack)
                        ans.append(stack[:])
                    else:
                        dfs(i, n, k, stack, ans)
                    stack.pop()
        dfs(1, n, k, stack, ans)
        return ans
"""

# recursive 464ms
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                ans.append(elements[:])
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        dfs([], 1, k)
        return ans
"""
  
# itertools.combinations 60ms  
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        return list(combinations(nums, k))

n = 4
k = 2
ret = Solution()
print(ret.combine(n, k))