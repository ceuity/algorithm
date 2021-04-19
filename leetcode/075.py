class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

"""
네덜란드 국기 정렬 문제.
실제로는 red, white, blue를 각각 0, 0, len(nums)만큼 두고 풀어야 하나 파이썬 내장 정렬 알고리즘으로도 풀 수 있다.
"""