from itertools import combinations

if __name__ == "__main__":
    N, M = map(int, input().split())

    comb = list(combinations(range(1, N + 1), M))
    for i in comb:
        print(" ".join(map(str, i)))
