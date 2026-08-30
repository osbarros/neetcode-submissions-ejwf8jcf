class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsAndIndexes = {}
        for i, n in enumerate(nums):
            if (target - n) in numsAndIndexes:
                return [numsAndIndexes[(target - n)], i]
            if n not in numsAndIndexes:
                numsAndIndexes[n] = i




