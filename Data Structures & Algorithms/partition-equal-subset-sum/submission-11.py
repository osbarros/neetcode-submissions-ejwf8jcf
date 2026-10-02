class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        half = int(totalSum / 2)
        if totalSum % 2 != 0:
            return False
        dp = [False for _ in range(half + 1)]
        dp[0] = True

        for num in nums:
            for j in range(len(dp) - 1, num -1, -1):
                skip = dp[j]
                take = dp[j - num]
                dp[j] = skip or take
        
        return dp[-1]
