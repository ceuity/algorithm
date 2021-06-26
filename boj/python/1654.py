import sys

if __name__ == "__main__":
    K, N = map(int, input().split())
    cable_list = []
    for _ in range(K):
        cable_list.append(int(sys.stdin.readline()))
    start = 1
    end = max(cable_list)
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for cable in cable_list:
            temp += cable // mid
        if temp >= N:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
