class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = [0]
        currSum = 0
        for n in nums:
            currSum += n
            prefixSum.append(currSum)
            

        freq = defaultdict(int)

        count = 0

        for p in prefixSum:
            if freq[p - k] > 0:
                count += freq[p - k] 
            freq[p] += 1

        return count
        





