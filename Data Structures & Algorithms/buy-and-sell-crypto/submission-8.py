class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_so_far:
                min_so_far = price

            profit = price - min_so_far
            if profit > max_profit:
                max_profit = profit
        
        return max_profit