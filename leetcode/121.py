# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 00:25:45 2021

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = -1
        
        for price in prices:
            if min_price == -1:
                min_price = price
            if price < min_price:
                min_price = price
            profit = max(profit, price - min_price)
        return profit