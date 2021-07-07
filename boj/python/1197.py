import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

if __name__ == "__main__":
    # 정점, 간선
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        # A정점이 B정점과 C의 가중치로 연결
        A, B, C = map(int, sys.stdin.readline().split())
        graph.append([A, B, C])
    # Kruskal 알고리즘을 위한 정렬
    graph = sorted(graph, key=lambda x: x[2])
    # Union-Find로 Cycle 탐색
    parents = [i for i in range(V + 1)]

    def find(n):
        if parents[n] == n:
            return n
        else:
            return find(parents[n])

    def union(x, y):
        x = find(x)
        y = find(y)
        if y < x:
            parents[x] = y
        else:
            parents[y] = x

    answer = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            answer += c
    print(answer)
