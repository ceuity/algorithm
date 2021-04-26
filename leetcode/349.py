from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

"""
합집합을 구하는 문제. set의 intersection method를 이용해서도 풀이가 가능하다.
"""