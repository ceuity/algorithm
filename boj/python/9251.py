if __name__=="__main__":
    str1 = list(input())
    str2 = list(input())
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
    print(max(max(dp)))

"""
LCS(Longest Common Subsequence)라는 알고리즘이 있어서 위키백과를 보고 그대로 코드로 옮겨서 풀었다.
"""