class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majorityElement = nums[0]
        for n in nums:
            if n == majorityElement:
                count += 1
            else: 
                count -= 1

            if count == 0:
                majorityElement = n
                count = 1
        
        return majorityElement