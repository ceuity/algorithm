# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:51:31 2021

"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dicts = {}
        for i in jewels:
            if i not in dicts:
                dicts[i] = 0
        for j in stones:
            if j in dicts:
                dicts[i] += 1
        return sum(dicts.values())
    
"""
이 문제는 key, value 쌍 구조인 딕셔너리를 이용하여 해결하는 가장 기본적인 문제이다.
딕셔너리의 jewels를 dict에 입력해두고 stones에서 jewels에 있으면 count를 +1 하여 해결하였다.
"""