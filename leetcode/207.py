# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 01:14:51 2021

"""

from collections import defaultdict
from typing import List

# 808ms
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for i in prerequisites:
            if i[0] == i[1]:
                return False
            if i[::-1] in prerequisites:
                return False
            courses[i[1]].append(i[0])
        for key, values in courses.items():
            for value in values:
                start = value
                curr = start
                while curr >= 0:
                    if courses[curr]:
                        curr = courses[curr][0]
                    else:
                        curr = -1
                    if curr == start:
                        return False
        return True

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        
        # print(graph)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True
"""

numCourses = 2
#prerequisites = [[1,0],[0,2],[2,1]]
#prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
prerequisites = [[1,0],[0,1]]
ret = Solution()
print(ret.canFinish(numCourses, prerequisites))

"""
어떻게 짜야 할지 로직은 알겠는데 그걸 코드로 구현하기가 너무 어려웠다.
다른 사람 코드 보고나니 어떻게 해야 할지 감이 잡히기 시작했다.
나중에 다시 한번 풀어봐야겠다.
"""