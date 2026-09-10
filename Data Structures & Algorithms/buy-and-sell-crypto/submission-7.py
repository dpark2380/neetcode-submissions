class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0

        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[left]

            if profit > ans:
                ans = profit

            if prices[i] < prices[left]:
                left = i
            
            profit = prices[i + 1] - prices[left]
            if profit > ans:
                ans = profit
        
        return ans