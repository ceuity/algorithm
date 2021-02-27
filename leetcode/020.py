# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:56:24 2021

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        if stack:
            return False
        return True
        
s = "()[]{}"
ret = Solution()
print(ret.isValid(s))

"""
이 문제를 어떻게 풀어야 할지 그림은 머릿속에 그려졌지만
그걸 어떻게 코드로 나타내야 할지 잘 떠오르지 않았다.
괄호를 하나씩 다 비교해야 하나 싶었는데 딕셔너리를 이용해서
table을 만든 후 if in을 이용하여 쉽게 비교할 수 있었다.
나머지는 닫는 기호가 아니면 stack에 push하고,
닫는 기호를 만났을 때 stack.pop() 한 값이 같으면 유효한 괄호이다.
"""