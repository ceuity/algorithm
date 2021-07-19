import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    answer = 0
    N, K = map(int, input().split())
    gems = []
    for _ in range(N):
        M, V = map(int, sys.stdin.readline().split())
        heappush(gems, [M, V])
    bags = []
    for _ in range(K):
        C = int(sys.stdin.readline())
        heappush(bags, C)
    temp = []
    for bag in bags:
        while gems and gems[0][0] <= bag:
            m, v = heappop(gems)
            heappush(temp, -v)
        if temp:
            answer += -heappop(temp)
    print(answer)