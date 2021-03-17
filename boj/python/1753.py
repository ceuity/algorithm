# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:06:59 2021

"""

from collections import defaultdict
import sys
import heapq

if __name__=="__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    K = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    def Dijkstra(start):
        q = [[0, start]]
        dp = [float('inf') for _ in range(V + 1)]
        dp[start] = 0
        while q:
            cost, curr = heapq.heappop(q)
            if dp[curr] < cost:
                continue
            for v, w in graph[curr]:
                if dp[v] > cost + w:
                    dp[v] = cost + w
                    heapq.heappush(q, ([cost + w, v]))
        for i in range(1, V + 1):
            print("INF" if dp[i] == float('inf') else dp[i])

    Dijkstra(K)

"""
처음으로 풀어보는 다익스트라 문제였다. 첫 시도에선 시간초과가 불필요한 계산을 제거했는데도 불구하고 계속 시간초과였다.
방문한 노드도 체크해주어야 하는 줄 알았는데 그럴 필요도 없었고, 가중치를 업데이트 할 때 바로바로 해야 힙에 더 안들어가는 것 같다.
"""