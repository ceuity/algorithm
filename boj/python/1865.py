from collections import defaultdict
from heapq import heappop, heappush
import sys


def solution():
    N, M, W = map(int, input().split())
    branchs = [float('inf')] * (N + 1)
    graph = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().strip().split())
        graph[S].append([E, -T])

    #벨만-포드 알고리즘
    def bellman_ford(n, graph, branchs):
        branchs[n] = 0
        for start in range(N):
            for v in range(1, N+1):
                for next, cost in graph[v]:
                    if branchs[next] > branchs[v] + cost:
                        branchs[next] = branchs[v] + cost
                        if start == N-1:
                            print("YES")
                            return
        print("NO")
        return

    bellman_ford(N, graph, branchs)


if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        solution()