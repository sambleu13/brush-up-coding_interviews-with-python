# solution using arrays
# time complexity O(N^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = profit = 0

        def get_profit(self, prices, base):
            profit = 0
            for price in prices:
                print(prices[0], len(prices))
                if price > base:
                    sell_price = price - base
                    if sell_price > profit:
                        profit = sell_price
            return profit


        if len(prices) <= 1:
            return 0
        for i, buy_price in enumerate(prices):
            profit = get_profit(self, prices[i:], buy_price)
            if profit > max_profit:
                max_profit = profit
        return max_profit

        
