class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            else:
                profit_today = prices[i]-min_price
                if profit_today > max_profit:
                    max_profit = profit_today
        return max_profit
        