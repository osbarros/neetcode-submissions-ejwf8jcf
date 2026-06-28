class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        triplets_zero_sum = []
        nums.sort()


        for i in range(len(nums) - 2):
            L = i + 1
            R = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return triplets_zero_sum
            while R > L:
                curSum = nums[i] + nums[L] + nums[R]
                if curSum > 0:
                    R -= 1
                elif curSum < 0:
                    L += 1
                elif curSum == 0:
                    triplets_zero_sum.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while R > L and nums[R] == nums[R + 1]:
                        R -= 1
                    while R > L and nums[L] == nums[L - 1]:
                        L += 1

        return triplets_zero_sum