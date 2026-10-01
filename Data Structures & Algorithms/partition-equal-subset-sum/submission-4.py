class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        half = int(totalSum / 2)
        if totalSum % 2 != 0:
            return False
        prevRow = [False for _ in range(half + 1)]
        prevRow[0] = True
        
        for i in range(1, len((nums))):
            curRow = [False for _ in range(half + 1)]
            for j in range(len(prevRow)):
                skip = prevRow[j]
                take = skip
                if j >= nums[i - 1]:
                    take = prevRow[j - nums[i - 1]]
                curRow[j] = skip or take
            prevRow = curRow

        return prevRow[-1]
