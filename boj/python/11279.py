import sys
import heapq

def solution():
    N = int(input())
    max_heap = []
    for _ in range(N):
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            if max_heap:
                print(-heapq.heappop((max_heap)))
            else:
                print(0)
        else:
            heapq.heappush(max_heap, -n)

if __name__ == "__main__":
    solution()