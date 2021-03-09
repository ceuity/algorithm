# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:01:58 2021

"""

if __name__ == '__main__':
    n = int(input())
    w = [0]
    for _ in range(n):
        w.append(int(input()))
    dp =[0]
    dp.append(w[1])
    if n > 1:
        dp.append(w[1] + w[2])
    for i in range(3, n + 1):
        dp.append(max(dp[i-3] + w[i-1] + w[i], dp[i-2] + w[i], dp[i-1]))
    print(dp[n])

"""
이전의 계단 오르기랑 비슷한 문제였으나 푸는 방법이 조금 달랐다.
각 숫자에서 점화식을 구한 뒤 일반화 시켜주는 방향으로 문제를 해결했다.
"""