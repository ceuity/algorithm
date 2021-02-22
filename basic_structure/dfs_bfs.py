# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:42:09 2021

@author: EVer
"""

def dfs_recursive(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs_recursive(w, visited)
    return visited

def dfs_iterative(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited

def bfs_iterative(start_v):
    visited = []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                queue.append(w)
    return visited

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
    }
visited = []

print(dfs_recursive(1))
print(dfs_iterative(1))
print(bfs_iterative(1))
