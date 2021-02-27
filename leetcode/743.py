# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 01:15:34 2021

"""

from typing import List
from collections import defaultdict

"""
class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dfs(v, visited, cost):
            if v == n:
                return cost
            for i in graph[v]:
                if i not in visited:
                    visited.append(i)
                    cost += dp[v-1][i-1]
                    return dfs(i, visited, cost)
                    
        ans = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        graph = defaultdict(list)
        for src, dest, time in times:
            dp[src-1][dest-1] = time
            graph[src].append(dest)
        dfs(k, [k], 0)
        if ans == 0:
            return (-1)
        return ans
"""

class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for src, dest, cost in times:
            graph[src].append((dest, cost))
        
        Q = [(0, k)]
        dist = defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for dest, cost in graph[node]:
                    alt = time + cost
                    heapq.heappush(Q, (alt, dest))
        
        if len(dist) == n:
            return max(dist.values())
        return -1        

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ret = Solution()
print(ret.networkDelayTime(times, n, k))

"""
처응에 dfs로 푸는 문제인 줄 알고 열심히 풀었는데 알고보니 
우선순위 큐를 이용한 다익스트라 알고리즘으로 푸는 문제였다.
"""
