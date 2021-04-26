import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def solution(n):
    if n == 1:
        return dp[1]
    elif n == 2:
        return dp[2]
    else:
        if not dp[n]:
            dp[n] = solution(n-1) + solution(n-2)
        return dp[n]

if __name__ == "__main__":
    n = int(input())
    dp = defaultdict(int)
    dp[1] = 1
    dp[2] = 2
    print(solution(n) % 10007)