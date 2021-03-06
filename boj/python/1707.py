# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:20:09 2021

"""

from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
	k = int(input())

	def bfs():
		vertex, edge = map(int, input().split())
		graph = defaultdict(list)
		visited = [0 for _ in range(vertex)]
		for _ in range(edge):
			start, end = map(int, input().split())
			graph[start].append(end)
			graph[end].append(start)
		q = deque([1])
		visited[0] = 1
		while q:
			curr = q.popleft()
			vertex_list = graph[curr]
			for v in vertex_list:
				if visited[v-1] == 0:
					visited[v-1] = visited[curr-1] * -1
					q.append(v)
				elif visited[v-1] == visited[curr-1]:
					return ("NO")
			if not q:
				for i in range(len(visited)):
					if visited[i] == 0:
						q.append(i+1)
						visited[i] = 1
						break
		return ("YES")

	for _ in range(k):
		print(bfs())
"""
각 정점의 간선을 딕셔너리를 이용해 양방향으로 연결해준 뒤, 해당 정점에서 연결된 정점을 모두 불러와서 현재 정점에 설정된 값과 반대되는 값을 넣어준다.
1과 -1 두 가지로 구분하여서 정점을 방문하는 도중에 현재 정점의 값과 연결된 정점의 값이 같으면 인접한 정점이 같은 집합에 속한 것으로 판단하여 NO를 출력하고 함수를 종료한다.
"""