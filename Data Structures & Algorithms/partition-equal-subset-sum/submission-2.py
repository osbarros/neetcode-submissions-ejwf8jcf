class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        half = int(totalSum / 2)
        if totalSum % 2 != 0:
            return False
        dp = [[False for _ in range(half + 1)] for _ in range(len(nums) + 1)]

        for x in range(len(nums) + 1):
            dp[x][0] = True

        
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                skip = dp[i - 1][j]
                take = skip
                if j >= nums[i - 1]:
                    take = dp[i - 1][j - nums[i - 1]]
                dp[i][j] = skip or take
        return dp[-1][-1]

