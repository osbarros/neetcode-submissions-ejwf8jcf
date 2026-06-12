class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        L = curSum = 0

        for R, num in enumerate(nums):
            curSum += num
            print(f"current sum: {curSum}")
            while(curSum >= target):
                length = min(R - L + 1, length)
                curSum -= nums[L]
                L += 1
                
        return 0 if length == float("inf") else length
        