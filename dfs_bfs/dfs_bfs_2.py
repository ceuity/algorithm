# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:39:55 2020

@author: EVer
"""
def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(0, len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    visited = [0 for i in range(n)]
    answer = 0
    
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)
