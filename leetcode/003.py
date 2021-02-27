# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:52:14 2021

"""

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque()
        ans = ""
        for char in s:
            if char not in dq:
                dq.append(char)
                if len(ans) < len(dq):
                      ans = "".join(dq)
            else:
                if len(ans) < len(dq):
                      ans = "".join(dq)
                while True:
                    if dq.popleft() == char:
                        break
                dq.append(char)
        return len(ans)
    
"""
이 문제는 스택을 이용하여 해결하였다.
스택에 문자를 하나씩 넣어두고 길이를 계산하여 최대 길이일 때만 정답을 갱신하고,
만약 중복된 문자가 나오면 스택에서 해당 문자가 나올 때 까지 이전 문자들을 제거하여,
스택에는 문자가 중복되지 않게 하였다. 문자열을 다 순회했을 때, 가장 길었던 정답의 길이를 반환한다.
"""