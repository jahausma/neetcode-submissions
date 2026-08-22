class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0

        for price in prices:
            
            # keep track of the min price as we go through
            if price < min_price:
                min_price = price

            # check if the profit is more for selling today
            elif price - min_price > profit:
                profit = price - min_price
        
        return profit
