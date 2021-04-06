# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:09:35 2021

"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num)
        for _ in range(k - 1):
            heapq.heappop(q)
        return -heapq.heappop(q)
    
"""
heap을 이용하면 쉽게 풀 수 있다.
"""