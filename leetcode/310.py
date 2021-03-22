# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:31:01 2021

"""

""" Time Limit Exceeded
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        dp = [float('inf') for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def check_height(start, min_height):
            visited = [0 for _ in range(n)]
            q = deque([start])
            height = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if visited[curr] == 0:
                        visited[curr] = 1
                        for node in graph[curr]:
                            if visited[node] == 0:
                                q.append(node)
                height += 1
                if height > min_height:
                    return float('inf')
            return height
                    
        for i in range(n):
            min_height = min(dp)
            dp[i] = check_height(i, min_height)
        answer = []
        for i in range(n):
            if dp[i] == min_height:
                answer.append(i)
        return answer
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        # 양방향 그래프 구성
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        # 루트 노드만 남을 때 까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            
        return leaves
    
"""
처음엔 모든 정점에서 깊이를 구한 후 비교하려고 했었는데 해당 방법으로는 시간 초과였다.
따라서 가장자리에서 리프 노드만 제거하는 방법으로 문제를 해결하였다.
"""
