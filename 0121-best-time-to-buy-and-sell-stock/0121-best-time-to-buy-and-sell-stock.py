class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for current in prices:
            if current < minimum:
                minimum = current
            profit = current - minimum
            if profit > max_profit:
                max_profit = profit
        return max_profit