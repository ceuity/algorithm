class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = bin(x ^ y)[2:]
        count = 0
        for num in dist:
            if num == '1':
                count += 1
        return count

"""
비트 연산의 toggle 특성을 이용하여 문제를 해결하였다.
"""