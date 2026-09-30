class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        half = int(totalSum / 2)
        if totalSum % 2 != 0:
            return False

        cache = [[None for _ in range(half + 1)] for _ in range(len(nums))]
        def dfs(i: int, currentSum: int):

            if currentSum > half:
                return False

            elif currentSum == half:
                return True


            if i == len(nums):
                return False

            if cache[i][currentSum] is not None:
                return cache[i][currentSum]

            skip = dfs(i + 1, currentSum)
            take = dfs(i + 1, currentSum + nums[i])

            cache[i][currentSum] = skip or take
            return cache[i][currentSum]

        return dfs(0, 0)
        
        



