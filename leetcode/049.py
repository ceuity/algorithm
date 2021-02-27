# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:13:23 2021

"""
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        
        
strs = ["3","3","3"]

ret = Solution()
print(ret.groupAnagrams(strs))