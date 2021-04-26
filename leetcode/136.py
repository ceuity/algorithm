class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num
        return n

"""
비트연산의 toggle 특성을 이용하여 문제를 해결하였다.
"""