from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

"""
try, except 문법을 이용하여 풀어보았다.
"""