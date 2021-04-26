import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10000)


def dfs(n, graph, visited):
    for v, cost in graph[n]:
        if visited[v-1] == -1:
            visited[v-1] = visited[n-1] + cost
            dfs(v, graph, visited)


def solution():
    V = int(input())
    graph = defaultdict(list)
    answer = []
    for _ in range(V):
        line = list(map(int, sys.stdin.readline().strip().split()[:-1]))
        for i in range(1, len(line), 2):
            graph[line[0]].append([line[i], line[i+1]])
    visited = [-1] * V
    visited[i-1] = 0
    dfs(i, graph, visited)

    index = visited.index(max(visited))
    visited = [-1] * V
    visited[index] = 0
    dfs(index+1, graph, visited)
    print(max(visited))


if __name__ == "__main__":
    solution()