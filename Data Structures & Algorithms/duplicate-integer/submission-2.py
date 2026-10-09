class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        distinctNumbers = set()

        for n in nums:
            if n in distinctNumbers:
                return True

            distinctNumbers.add(n)

        return False