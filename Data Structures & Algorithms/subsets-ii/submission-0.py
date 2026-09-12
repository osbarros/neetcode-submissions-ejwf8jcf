class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        subsets = []
        nums.sort()
        def helper(i, nums, curSet, subsets):
            if i == len(nums):
                subsets.append(curSet.copy())
                return 
            
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subsets)
            curSet.pop()
            while (i < len(nums) - 1 and nums[i] == nums[i + 1]):
                i += 1
            helper(i + 1, nums, curSet, subsets)

        helper(0, nums, curSet, subsets)
        return subsets