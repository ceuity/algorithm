# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 00:54:45 2021

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
ret = Solution()
print(ret.twoSum(s))