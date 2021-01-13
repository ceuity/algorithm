# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 02:04:29 2021

"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
    
    
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
ret = Solution()
print(ret.reorderLogFiles(logs=logs))