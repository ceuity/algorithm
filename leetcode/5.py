# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 02:00:14 2021

@author: EVer
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(str)
        while length > 0:
            for i in range(length):
                if str[i:length-1] == 