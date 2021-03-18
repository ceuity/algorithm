# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 02:26:15 2021

"""

import sys

if __name__=="__main__":
	input = sys.stdin.readline
	N, M = map(int, input().split())
	dist = [float('inf') for _ in range(N + 1)]
	edges = []
	for _ in range(M):
		A, B, C = map(int, input().split())
		edges.append([A, B, C])
	def bf(start):
		dist[start] = 0
		for i in range(N):
			for j in range(M):
				curr = edges[j][0]
				next_node = edges[j][1]
				cost = edges[j][2]
				if dist[next_node] > dist[curr] + cost:
					dist[next_node] = dist[curr] + cost
					if i == N - 1:
						return True
		return False

	negative_cycle = bf(1)
	if negative_cycle:
		print("-1")
	else:
		for i in range(2, N + 1):
			if dist[i] != float('inf'):
				print(dist[i])
			else:
				print('-1')
                
"""
다익스트라 알고리즘을 잘 익혀두었더니 다익스트라 알고리즘을 포함하는 벨만 포드 알고리즘은 좀 더 쉽게 이해가 된 것 같다.
결국 다익스트라 알고리즘은 최소힙을 이용하여 가중치가 작은 노드만 방문하는데 비해 벨만 포드 알고리즘은
N개의 노드를 M개의 간선 수 만큼 탐색하는 것 이기 때문에 벨만 포드 알고리즘이 더 큰 개념으로 볼 수 있다.
"""