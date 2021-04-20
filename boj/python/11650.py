import sys

if __name__ == "__main__":
    N = int(input())
    coords = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coords.append([x, y])
    coords.sort(key=lambda x: (x[0], x[1]))
    for x, y in coords:
        print(x, y)