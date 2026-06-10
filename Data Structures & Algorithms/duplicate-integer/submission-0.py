class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seewy = set()

        for n in nums:
            if n not in seewy:
                seewy.add(n)
            else: 
                return True
        
        return False