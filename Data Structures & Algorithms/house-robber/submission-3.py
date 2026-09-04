class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        maxSum = 0

        print(maxSum)

        while i <= len(nums) - 1:
            maxSum = max(nums[i] + dp[0], dp[1])
            print(f"maxSum now = {maxSum}, dp[0] = {dp[0]} and dp[1] = {dp[1]}")
            tmp = dp[1]
            dp[1] = maxSum
            dp[0] = tmp
            i += 1

        return maxSum
            