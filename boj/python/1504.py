# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:30:53 2021

"""

import sys
from collections import defaultdict
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    V1, V2 = map(int, input().split())
    dp = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]

    def Dijkstra(start):
        heap = []
        dp[start][start] = 0
        heapq.heappush(heap, [0, start])

        while heap:
            dist, curr = heapq.heappop(heap)
            if dp[start][curr] < dist:
                continue
            for v, w in graph[curr]:
                next_w = dp[start][curr] + w
                if next_w < dp[start][v]:
                    dp[start][v] = next_w
                    heapq.heappush(heap, [dp[start][v], v])

    first = Dijkstra(1)
    second = Dijkstra(V1)
    third = Dijkstra(V2)
    if dp[1][V1] == float('inf') or dp[V1][V2] == float('inf') or dp[V2][N] == float('inf'):
        ans = -1
    elif dp[1][V2] == float('inf') or dp[V2][V1] == float('inf') or dp[V1][N] == float('inf'):
        ans = -1
    else:
        ans = min(dp[1][V1] + dp[V1][V2] + dp[V2][N], dp[1][V2] + dp[V2][V1] + dp[V1][N])
    print(ans)
    
"""
다익스트라 문제에 대해 어느 정도 감을 잡은 것 같다. 기본 개념을 잘 익혀두자.
"""