if __name__=="__main__":
    n = int(input())
    lines = []
    dp = [0 for _ in range(n)]
    for _ in range(n):
        lines.append(list(map(int, input().split())))
    lines.sort()
    for i in range(n):
        for j in range(n):
            if lines[i][1] > lines[j][1]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
    print(n - max(dp))

"""
잘 생각해보니 A 또는 B 둘 중 하나를 정렬한 다음에 정렬하지 않은 쪽에서 LIS를 구하면 되는 문제였다.
"""