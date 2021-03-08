# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 00:28:07 2021

"""

if __name__=="__main__":
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(101)]
    dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n-1]) % 1000000000)
    
"""
처음에 문제가 이해가 안 되어서 다른 사람들의 풀이를 보고 했다.
결국 0~9가 있을 때 이 사이에서 N 자리의 계단수를 찾으라는 의미였다.
문제가 너무 불친절하다.
"""