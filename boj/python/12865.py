# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 02:41:49 2021

"""

if __name__=="__main__":
    N, K = map(int, input().split())
    bags = [[0, 0]]
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for _ in range(N):
        bags.append(list(map(int, input().split())))
    for i in range(1, N+1):
        for j in range(1, K+1):
            if j >= bags[i][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - bags[i][0]] + bags[i][1])
            else:
                dp[i][j] = dp[i-1][j]
    print(max(max(dp)))

"""
DP 문제인 건 알고 있었지만 기준을 어디로 잡아야 할지 잘 떠오르질 않았다.
견딜 수 있는 무게보다 적은 범위 내에서 하나의 [w, v]원소를 이용하여 구할 수 있는 무게의 조합을
전부 구해주는 방식으로 문제를 해결하였다.
"""