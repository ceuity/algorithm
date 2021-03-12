if __name__=="__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    dp_f = [1 for _ in range(n)]
    dp_b = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp_f[i] = max(dp_f[i], dp_f[j] + 1)
    for i in reversed(range(n)):
        for j in reversed(range(i, n)):
            if sequence[i] > sequence[j]:
                dp_b[i] = max(dp_b[i], dp_b[j] + 1)
    print(max([x + y for x, y in zip(dp_f, dp_b)]) - 1)

"""
LIS를 양쪽에서 모두 구한 후 i번째 에서 두 개의 합 - 1 값이 가장 큰 값을 정답으로 했다.
"""