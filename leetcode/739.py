# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:44:40 2021

"""

from typing import List
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        days = 0
        if len(T) == 1:
            return [0]
        for i in range(len(T)):
            days = 0
            for j in range(i, len(T)):
                if T[i] < T[j]:
                    stack.append(days)
                    break
                elif j == len(T) - 1:
                    stack.append(0)
                else:
                    days += 1
        return (stack)
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # T 길이만큼의 answer list 생성
        answer = [0] * len(T)
        stack = []
        for i, temp in enumerate(T):
            # 현재 온도가 stack에 마지막에 저장되어 있는 온도보다 큰 경우
            while stack and temp > T[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)           
        return (answer)

T = [73, 74, 75, 71, 69, 72, 76, 73]               
ret = Solution()
print(ret.dailyTemperatures(T))


"""
이번 문제는 처음에 for문을 두 개 사용하여 시도했다가 시간초과가 나서 다른 방법을
찾아보니 stack을 이용하는 방법이었다. stack에 index를 저장해 두었다가 현재 온도보다
낮은 index의 온도는 index 차이 만큼을 반환해주면 되는 것이다.
"""