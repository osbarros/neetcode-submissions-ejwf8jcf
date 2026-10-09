class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = [1]

        currProduct = nums[0]

        for i in range(1, len(nums)):
            products.append(currProduct)
            currProduct *= nums[i]

        currProduct = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            products[i] = products[i] * currProduct
            currProduct *= nums[i]

        return products