# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:26:56 2021

"""

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        t = defaultdict(list)
        for ticket in tickets:
            t[ticket[0]].append(ticket[1])
        for key, value in t.items():
            t[key] = sorted(value, reverse=True)
        start = ["JFK"]
        ans = []
        
        while start:
            curr = start[-1]
            
            if curr not in t or len(t[curr]) == 0:
                ans.append(start.pop())
            else:
                start.append(t[curr].pop())
        ans.reverse()
        return ans

""" DFS
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_count = collections.defaultdict(list)
        for t in tickets:
            tickets_count[t[0]].append(t[1])
    
        for dest_list in tickets_count.values():
            dest_list.sort(reverse=True)
            
        N = len(tickets)
        # print(tickets_count)
        ret = []
            
        def dfs(depart):
            
            while tickets_count[depart]:
                dfs(tickets_count[depart].pop())
                
            ret.append(depart)
         
        dfs('JFK')
        return ret[::-1]
"""

            
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
ret = Solution()
print(ret.findItinerary(tickets))

"""
프로그래머스에도 같은 문제가 있어서 풀었던 기억이 있었다.
하지만 어느 정도만 기억했고 정확한 풀이 방법이 기억이 나질 않아 찾아보았다.
"""