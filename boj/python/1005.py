import sys
from collections import defaultdict, deque

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        build_times = [0] + list(map(int, input().split()))
        dp = [0 for _ in range(N + 1)]
        tech_tree = defaultdict(list)
        degree = defaultdict(int)

        for _ in range(K):
            start, end = map(int, sys.stdin.readline().split())
            tech_tree[start].append(end)
            degree[end] += 1

        wins = int(input())

        q = deque()
        for i in range(1, N+1):
            if degree[i] == 0:
                q.append(i)
                dp[i] = build_times[i]

        while q:
            curr = q.popleft()
            for i in tech_tree[curr]:
                degree[i] -= 1
                dp[i] = max(dp[i], build_times[i] + dp[curr])
                if degree[i] == 0:
                    q.append(i)

        print(dp[wins])
