from collections import Counter

# 48ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

# 32ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False

"""
처음엔 간단하게 sorted 함수를 이용하여 풀었으나, Counter 함수를 이용했을 때 더 빨랐다.
"""