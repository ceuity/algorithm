# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 01:20:54 2021

"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left_stack = [0 for _ in range(len(height))]
        right_stack = [0 for _ in range(len(height))]
        left_max = 0
        right_max = 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            left_stack[i] = left_max - height[i]
        for i in range(len(height) - 1, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            right_stack[i] = right_max - height[i]
        for i in range(len(height)):
            ans += min(left_stack[i], right_stack[i])
        return ans
        
height = [4,2,0,3,2,5]

ret = Solution()
print(ret.trap(height))