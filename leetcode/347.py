# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:44:29 2021

"""

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        ans = []
        for i in nums:
            nums_dict[i] += 1
        nums_sorted = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            ans.append(nums_sorted[i][0])
        return ans


nums = [1, 1, 1, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3]
k = 2
ret = Solution()
print(ret.topKFrequent(nums, k))
