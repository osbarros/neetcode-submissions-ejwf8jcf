class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        prevRow = [0 for _ in range(2 * totalSum + 1)]
        prevRow[totalSum] = 1
        if target > totalSum or target < (totalSum * -1):
            return 0

        for i in range(len(nums)):
            curRow = [0 for _ in range(2 * totalSum + 1)]
            for j in range(len(prevRow)):
                addition = subtraction = 0
                if j - nums[i] >= 0:
                    addition = prevRow[j - nums[i]]
                if j + nums[i] < len(prevRow):
                    subtraction = prevRow[j + nums[i]]
                curRow[j] = addition + subtraction
            prevRow = curRow
        
        return prevRow[target + totalSum]