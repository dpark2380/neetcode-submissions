class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = prices[0]
        curmax = 0

        for price in prices:
            if price < curmin:
                curmin = price

            profit = price - curmin
            if profit > curmax:
                curmax = profit
        
        return curmax