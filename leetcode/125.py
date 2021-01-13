# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:15:03 2021

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]
    
    
s = "A man, a plan, a canal: Panama"
ret = Solution()
print(ret.isPalindrome(s))