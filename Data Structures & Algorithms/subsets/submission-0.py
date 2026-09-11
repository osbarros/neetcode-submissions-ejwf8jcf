class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []

        def helper(i, curSet, subsets, nums):
            if i == len(nums):
                subsets.append(curSet.copy())
                return subsets
            
            
            curSet.append(nums[i])
            helper(i + 1, curSet, subsets, nums)


            curSet.pop()
            helper(i + 1, curSet, subsets, nums)
        
        helper(0, curSet, subsets, nums)
        return subsets

