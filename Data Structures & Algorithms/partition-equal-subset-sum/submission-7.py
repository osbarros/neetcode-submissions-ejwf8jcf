class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        half = int(totalSum / 2)
        if totalSum % 2 != 0:
            return False
        currentSum = [False for _ in range(half + 1)]
        currentSum[0] = True

        for i in range(len(nums)):
            for j in range(len(currentSum) - 1, -1, -1):
                skip = currentSum[j]
                take = False
                if j >= nums[i]:
                    take = currentSum[j - nums[i]]
                
                currentSum[j] = skip or take
        
        return currentSum[-1]
