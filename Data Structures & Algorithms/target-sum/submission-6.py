class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        dp = [[0 for _ in range(2 * totalSum + 1)] for _ in range(len(nums) + 1)]
        dp[0][totalSum] = 1
        if target > totalSum or target < (totalSum * -1):
            return 0

        for i in range(1, len(nums) + 1):
            for j in range(len(dp[0])):
                addition = subtraction = 0
                if j - nums[i - 1] >= 0:
                    addition = dp[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] < len(dp[0]):
                    subtraction = dp[i - 1][j + nums[i - 1]]
                dp[i][j] = addition + subtraction
        
        return dp[len(nums)][target + totalSum]