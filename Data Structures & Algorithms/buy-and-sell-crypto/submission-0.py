class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = maxAmount = 0
        R = 1

        while R < len(prices):
            if prices[L] < prices[R]:
                maxAmount = max(maxAmount, prices[R] - prices[L])
            
            else:
                L = R

            R += 1
        
        return maxAmount