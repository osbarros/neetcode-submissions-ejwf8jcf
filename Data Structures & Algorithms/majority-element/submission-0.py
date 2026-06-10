class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_nums = {}
        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1
        
        return max(count_nums, key = count_nums.get)