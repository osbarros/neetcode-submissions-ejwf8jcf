class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        previous = None
        count = 0

        for R in range(len(nums)):

            if previous == nums[R]:
                count += 1
            
            else: 
                count = 0
            
            if count < 2:
                nums[L] = nums[R]
                L += 1

            
            previous = nums[R]

        return L