class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_double = nums.copy()
        for num in nums:
            nums_double.append(num)
        return nums_double