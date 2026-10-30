class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set()
        for n in nums:
            setNums.add(n)

        longestConsecutive = 0

        
        for i in range(len(nums)):
            count = 1
            j = 1
            n = nums[i]
            while n - j in setNums:
                count += 1
                setNums.remove(n - j)
                j += 1

            j = 1
            while n + j in setNums:
                count += 1
                setNums.remove(n + j)
                j += 1
            
            longestConsecutive = max(longestConsecutive, count)


        return longestConsecutive
        