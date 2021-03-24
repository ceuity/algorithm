# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:42:45 2021

"""

from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    visited = [-1 for _ in range(n + 1)]
    graph = defaultdict(list)
    q = deque([1])
    dist = 0
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if visited[curr] == -1:
                visited[curr] = dist
                for node in graph[curr]:
                    if visited[node] == -1:
                        q.append(node)
        dist += 1
    answer = visited.count(max(visited))
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))