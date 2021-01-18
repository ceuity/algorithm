# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:24:13 2021

"""

from itertools import combinations
from typing import List

"""
first_try timeout

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for comb in list(combinations(nums, 3)):
            if sum(comb) == 0 and sorted(comb) not in ans:
                ans.append(sorted(list(comb)))
        return ans
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
        
nums = [1,-1,-1,0]
ret = Solution()
print(ret.threeSum(nums))