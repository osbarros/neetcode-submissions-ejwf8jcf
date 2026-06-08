class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n

        partial = 0
        for i, n in enumerate(nums):
            
            if partial == (total-n)/2:
                return i
            partial += n
            
        return -1

        