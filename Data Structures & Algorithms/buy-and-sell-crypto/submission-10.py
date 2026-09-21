class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            profit = price - minPrice
            ans = max(ans, profit)

        return ans


