class Solution:
    def totalMoney(self, n: int) -> int:
        answer = 0
        for i in range(n):
            answer += (i % 7 + 1) + (i // 7)
        return answer