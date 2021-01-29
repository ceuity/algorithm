# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:34:05 2021

Test
"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        seen = set()
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            print(stack, seen)
        return ''.join(stack)
        
s = "cbacdcbc"
ret = Solution()
print(ret.removeDuplicateLetters(s))

"""
처음에 이 문제를 어떻게 풀어야 하는 건지 풀이를 봐도 전혀 감이 오질 않았다.
유튜브와 각종 풀이들을 보고 나서야 어떤 문제인지 이해했다.
결국 시작 문자를 기준으로 중복을 제외하고 사전순으로 가장 가까운 문자의 조합을 만드는 것이었다.
"""
