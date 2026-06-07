class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R, num in enumerate(nums):
            if R - L > k:
                window.discard(nums[L])
                L += 1
                
            if num in window:
                return True
            
            window.add(num)

        return False