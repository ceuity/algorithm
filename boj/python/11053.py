# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:06:18 2021

"""

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
    print(max(dp))

"""
단순하게 생각해보면 그냥 O(N^2)으로 풀리는 문제이다.
DP 문제길래 N^2으로 안풀리는 줄 알았는데 너무 어렵게 생각했던 것 같다.
"""