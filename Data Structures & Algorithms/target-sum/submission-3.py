class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i: int, currentSum: int):
            if i == len(nums):
                if currentSum == target:
                    return 1
                return 0

            if (i, currentSum) in cache:
                return cache[(i, currentSum)]
            addition = dfs(i + 1, currentSum + nums[i])
            subtraction = dfs(i + 1, currentSum - nums[i])

            cache[(i, currentSum)] = addition + subtraction

            return cache[(i, currentSum)]

        return dfs(0, 0)
