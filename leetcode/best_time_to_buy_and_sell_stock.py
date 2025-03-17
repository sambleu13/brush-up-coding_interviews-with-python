# solution using arrays and subhelper function with Maxheap
# time complexity O(N^2)
import heapq as hp

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = [0]

        def get_profit(self, prices, base):
            profit = [0]
            for price in prices:
                if base < price:
                    hp.heappush(profit, -(price - base))
            return -hp.heappop(profit)


        if len(prices) <= 1:
            return 0
        for i, buy_price in enumerate(prices):
            hp.heappush(max_profit, -get_profit(self, prices[i+1:], buy_price))
            # print(buy_price, profit, array)
        return -hp.heappop(max_profit)
