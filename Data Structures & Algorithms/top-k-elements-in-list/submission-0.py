class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1


        sortedFreq = sorted(freq.items(), key = lambda item: item[1], reverse = True)

        return [item[0] for item in sortedFreq[0:k]]