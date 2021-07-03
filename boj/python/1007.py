import sys
import math
from itertools import permutations, combinations


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        coords = []
        x_total = 0
        y_total = 0
        for _ in range(N):
            x, y = map(int, sys.stdin.readline().split())
            x_total += x
            y_total += y
            coords.append([x, y])

        answer = float("inf")
        vectors = list(combinations(coords, N // 2))
        for vector in vectors[: len(vectors) // 2]:
            x1_total = 0
            y1_total = 0
            for x1, y1 in vector:
                x1_total += x1
                y1_total += y1

            x2_total = x_total - x1_total
            y2_total = y_total - y1_total

            answer = min(
                answer,
                math.sqrt((x2_total - x1_total) ** 2 + (y2_total - y1_total) ** 2),
            )
        print(answer)
