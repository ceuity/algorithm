# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:02:35 2021

"""

from heapq import heappush, heappop
import sys
from collections import defaultdict

if __name__=="__main__":
	input = sys.stdin.readline
	n = int(input())
	m = int(input())
	graph = defaultdict(list)
	for _ in range(m):
		a, b, c = map(int, input().split())
		graph[a].append([b, c])
		
	def Dijkstra(start):
		dp = [float('inf') for _ in range(n + 1)]
		dp[start] = 0
		q = []
		heappush(q, [0, start])
		while q:
			cost, curr = heappop(q)
			if dp[curr] < cost:
				continue
			for v, w in graph[curr]:
				next_cost = dp[curr] + w
				if next_cost < dp[v]:
					dp[v] = next_cost
					heappush(q, [dp[v], v])
		for i in range(1, len(dp)):
			if dp[i] == float('inf'):
				dp[i] = 0
		print(' '.join(map(str, dp[1:])))
	
	for i in range(1, n + 1):
		Dijkstra(i)

"""
플로이드 와샬은 O(V^3)의 시간복잡도를 가진다고 하지만 Dijkstra를 V번 만큼 하면
O(V^2logE)의 시간복잡도를 가진다고 생각하는데 맞는지 모르겠다.
"""