import heapq
import sys

if __name__ == "__main__":
    N = int(input())
    q = []
    for _ in range(N):
        n = int(sys.stdin.readline().strip())
        if n == 0:
            if not q:
                print(0)
            else:
                print(heapq.heappop(q))
        else:
            heapq.heappush(q, n)