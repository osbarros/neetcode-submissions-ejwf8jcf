class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxAmount = curAmount = 0
        
        for n in nums:
            if n == 1:
                curAmount +=1
                maxAmount = max(curAmount, maxAmount)
            else: 
                curAmount = 0
            
        return maxAmount
        