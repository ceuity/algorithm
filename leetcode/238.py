# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:12:45 2021

"""
import math
from typing import List

"""
first try Timeout

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(len(nums)):
            target = nums.pop(0)
            ans.append(math.prod(nums))
            nums.append(target)
        return ans
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        ans = []
        p = 1
        for i in range(len(nums)):
            left_prod.append(p)
            p *= nums[i]
        p = 1
        for i in reversed(range(len(nums))):
            right_prod.append(p)
            p *= nums[i]
        right_prod = right_prod[::-1]
        for i in range(len(nums)):
            ans.append(left_prod[i] * right_prod[i])
        return ans
        
nums = [4,5,1,8,2]
ret = Solution()
print(ret.productExceptSelf(nums))