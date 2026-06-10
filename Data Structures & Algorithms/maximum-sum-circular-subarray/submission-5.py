class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        visited = set()
        curSumMax = curSumMin = 0
        maxSum = minSum = nums[0]
        totalSum = 0


        for n in nums: 
            curSumMin = min(curSumMin, 0)
            curSumMax = max(curSumMax, 0)
            curSumMin +=n
            curSumMax +=n
            totalSum += n
            minSum = min(minSum, curSumMin)
            maxSum = max(maxSum, curSumMax)

        if maxSum < 0:
            return maxSum

        else:
            return max(maxSum, totalSum - minSum)