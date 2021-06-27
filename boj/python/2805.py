from collections import Counter


if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = Counter(map(int, input().split()))
    start = 0
    end = max(trees)
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for tree, n in trees.items():
            if tree > mid:
                temp += (tree - mid) * n
            if temp > M:
                break
        if temp >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(end)