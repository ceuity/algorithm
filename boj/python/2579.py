# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:00:03 2021

"""

if __name__=="__main__":
    n = int(input())
    step = [0 for _ in range(301)]
    dp = [0 for _ in range(301)]

    for i in range(n):
        step[i] = int(input())

    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    dp[2] = max(step[0] + step[2], step[1] + step[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
    print(dp[n-1])

"""
현재 계단에 도달할 수 있는 방법 중 큰 값을 넣도록 했다.
마지막 계단을 반드시 밟아야 하므로 마지막 현재 위치를 기준으로 이전 값들 중 최댓값을 찾도록 했다.
계단오르기 어렵다.
"""