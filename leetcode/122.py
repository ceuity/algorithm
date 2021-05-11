# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         answer = []
#         min_price = float('inf')
#         max_profit = 0
#         for price in prices:
#             min_price = min(min_price, price)
#             profit = price - min_price
#             if profit > max_profit:
#                 max_profit = profit
#             else:
#                 answer.append(max_profit)
#                 max_profit = 0
#                 min_price = price
#         if max_profit:
#             answer.append(max_profit)
#         return sum(answer)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i + 1] - prices[i], 0)
        return max_profit

"""
생각해보니 간단하게 풀 수 있는 문제였다. 그냥 매 번 차익만큼을 더해주면 되는 문제였다.
"""