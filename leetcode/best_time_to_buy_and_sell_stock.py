# solution using heap and max function
# time complexity O(N)
import heapq as hp

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price, max_profit = prices[0], [0]

        if len(prices) <= 1:
            return 0

        for price in prices[1:]:
            hp.heappush(max_profit, -(price - sell_price))
            sell_price = min(sell_price, price)
            
        return -hp.heappop(max_profit)
