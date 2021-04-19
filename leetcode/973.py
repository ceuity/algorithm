from math import sqrt
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))

        return points[:k]

"""
lambda식을 이용하여 주어진 조건에 맞게 정렬한 후 주어진 갯수 만큼 return하여 해결하였다.
"""