class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = 0
        R = pos = len(nums) - 1
        nums_square = [0] * len(nums)
        

        while R >= L:
            if abs(nums[R]) > abs(nums[L]):
                nums_square[pos] = nums[R] ** 2
                R -= 1
            else:
                nums_square[pos] = nums[L] ** 2
                L += 1
            pos -= 1

        return nums_square
            