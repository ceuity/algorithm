# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:01:09 2021

"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(nums, stack):
            ans.append(stack[:])
            if not nums:
                return
            for i, num in enumerate(nums):
                if num not in stack:
                    stack.append(num)
                    dfs(nums[i+1:], stack)
                    stack.pop()
        dfs(nums, [])
        return ans

nums = [1,2,3]
ret = Solution()
print(ret.subsets(nums))

"""
dfs 문제가 아직 잘 익혀지지가 않아서 감각적으로 풀어버렸다.
풀고 나서 다른 사람의 풀이를 보니까 비트연산을 해서 푼 사람도 있었다.
생각해보니 2^n개 만큼의 비트를 index로 보고 해당 비트가 가질 수 있는 모든 경우의 수의
인덱스에 있는 요소들을 넣어줘도 해결할 수 있는 문제였다. 아마 비트연산이 가장 빠를 것 같다.
"""