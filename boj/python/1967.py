import sys
from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(start, graph, n):
    visited = [float('inf')] * n
    visited[start - 1] = 0
    heap = [[0, start]]
    while heap:
        cost, curr = heappop(heap)
        if visited[curr - 1] < cost:
            continue
        for next, w in graph[curr]:
            if visited[next - 1] > visited[curr - 1] + w:
                visited[next - 1] = visited[curr - 1] + w
                heappush(heap, [visited[next - 1], next])
    return visited


def solution():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        p, c, w = map(int, sys.stdin.readline().strip().split())
        graph[p].append([c, w])
        graph[c].append([p, w])
    visited = dijkstra(1, graph, n)
    index = visited.index(max(visited))
    visited = dijkstra(index + 1, graph, n)
    print(max(visited))


if __name__ == "__main__":
    solution()
