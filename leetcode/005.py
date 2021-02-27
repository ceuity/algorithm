# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 02:00:14 2021

@author: EVer
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        const = length + 1
        while length > 0:
            for i in range(const - length):
                temp = s[i:i+length]
                if temp == temp[::-1]:
                    return temp;
            length -= 1
                    
s = "babad"

ret = Solution()
print(ret.longestPalindrome(s))