class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse() # cant set this equal to anything as the .function() edits the original price
        profit = 0

        for i in range(len(prices)):
            sell = prices[i]
            min_buy = min(prices[i:])
            
            temp = sell - min_buy

            if temp > profit:
                profit = temp
        
        return profit