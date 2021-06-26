import sys

def solution():
    N, H = map(int, input().split())
    up = [0 for _ in range(H+1)]
    down = [0 for _ in range(H+1)]

    min_count = N
    range_count = 0
    for i in range(N):
        if i % 2 == 0:
            down[int(sys.stdin.readline().strip())] += 1
        else:
            up[int(sys.stdin.readline().strip())] += 1
    for i in range(H - 1, 0, -1):
        down[i] += down[i + 1]
        up[i] += up[i + 1]
    for i in range(1, H + 1):
        if min_count > (down[i] + up[H - i + 1]):
            min_count = (down[i] + up[H - i + 1])
            range_count = 1
        elif min_count == (down[i] + up[H - i + 1]):
            range_count += 1

    print(min_count, range_count)


if __name__ == "__main__":
    solution()