class Solution:

    def sumHouses(self, nums: List[int], i: int) -> int:
        if i > len(nums) - 1:
            return 0
        
        elif i == len(nums) - 1:
            return nums[i]

        elif i in self.cache:
            return self.cache[i]

        else:
            self.cache[i] = max(nums[i] + self.sumHouses(nums, i + 2), self.sumHouses(nums, i + 1))
        return self.cache[i]

    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return self.sumHouses(nums, 0)