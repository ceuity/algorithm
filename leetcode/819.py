# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:26:07 2021

"""

from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ret = {}
        split_list = re.sub('[^a-z]', ' ', paragraph.lower()).split()
        for ban in banned:
            while ban in split_list:
                split_list.remove(ban)
        for s in split_list:
            if s not in ret:
                ret[s] = 1
            else:
                ret[s] += 1
        print(ret)
        return max(ret.keys(), key=lambda x:ret[x])
    
    
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

ret = Solution()
print(ret.mostCommonWord(paragraph, banned))