import sys
from collections import Counter


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.extend(list(map(int, sys.stdin.readline().split())))
    counts = Counter(grid)
    answer_time = float('inf')
    answer_height = 0
    for target in range(max(grid), -1, -1):
        block = B
        times = 0
        for h, n in counts.items():
            if h > target:
                times += 2 * (h - target) * n
                block += (h - target) * n
            else:
                times += (target - h) * n
                block -= (target - h) * n
        if block >= 0:
            if answer_time > times:
                answer_time = times
                answer_height = target
    print(answer_time, answer_height)