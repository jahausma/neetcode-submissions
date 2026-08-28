class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit  = 0 
        minSoFar = prices[0]

        for i in range(len(prices)):
            if i > 0:
                maxProfit = max(prices[i] - minSoFar, maxProfit)
            minSoFar = min(prices[i], minSoFar)
        
        return maxProfit