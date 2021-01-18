# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:00:28 2021

"""

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])
        
nums = [1,4,3,2]
ret = Solution()
print(ret.arrayPairSum(nums))