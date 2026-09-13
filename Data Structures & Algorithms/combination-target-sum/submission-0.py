class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        curComb = []
        def helper(i, curComb, combinations, curSum, target, nums):
            if curSum == target:
                combinations.append(curComb.copy())
                return 

            if curSum > target:
                return
            
            for j in range(i, len(nums)):
                curComb.append(nums[j])
                curSum += nums[j]
                helper(j, curComb, combinations, curSum, target, nums)
                curSum -= nums[j]
                curComb.pop()

        helper(0, curComb, combinations, 0, target, nums)
        return combinations