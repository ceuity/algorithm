# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:28:58 2021

"""

import sys
from collections import defaultdict
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    T = int(input())
    
    def find_destination():
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = defaultdict(list)
        dp = [0 for _ in range(n + 1)]
        pred = []
        ans = []
        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a].append([b, d])
            graph[b].append([a, d])
        for _ in range(t):
            pred.append(int(input()))
        pred.sort()
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        def Dijkstra(start):
            dp[start][start] = 0
            heap = []
            heapq.heappush(heap, [0, start])

            while heap:
                dist, curr = heapq.heappop(heap)
                if dp[start][curr] < dist:
                    continue
                for v, w in graph[curr]:
                    next_dist = dp[start][curr] + w
                    if dp[start][v] > next_dist:
                        dp[start][v] = next_dist
                        heapq.heappush(heap, [dp[start][v], v])
        Dijkstra(s)
        Dijkstra(g)
        Dijkstra(h)
        for i in pred:
            if dp[s][i] != float('inf') and dp[s][i] == min(dp[s][g] + dp[g][h] + dp[h][i], dp[s][h] + dp[h][g] + dp[g][i]):
                ans.append(i)
        print(' '.join(map(str, ans)))
    for _ in range(T):
        find_destination()

"""
1504번이랑 거의 같은 유형의 문제
"""