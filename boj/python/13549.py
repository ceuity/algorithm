from collections import defaultdict
from heapq import heappop, heappush

if __name__ == "__main__":
    N, K = map(int, input().split())
    heap = [[0, N]]
    visited = defaultdict(lambda: float("inf"))
    while True:
        time, curr = heappop(heap)
        if curr == K:
            print(time)
            break
        if visited[curr] > time:
            if curr + 1 <= K:
                heappush(heap, [time + 1, curr + 1])
            if curr - 1 >= 0:
                heappush(heap, [time + 1, curr - 1])
            if curr < K:
                heappush(heap, [time, curr * 2])
            visited[curr] = time
