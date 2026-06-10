class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = R = 0
        previous = None
        
        for R in range(len(nums)):
            if nums[R] == previous:
                continue
            
            else:
                nums[L] = nums[R]
                L += 1
            previous = nums[R]

        
        return L
            