class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_double = nums.copy()
        print(nums_double)
        for num in nums:
            nums_double.append(num)
        return nums_double