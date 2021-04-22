import sys
from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split())
    name_list = defaultdict(int)
    answer = []
    for _ in range(N):
        name_list[(sys.stdin.readline().strip())] = 1
    for _ in range(M):
        temp = sys.stdin.readline().strip()
        if name_list[temp]:
            answer.append(temp)
    print(len(answer))
    answer.sort()
    for name in answer:
        print(name)