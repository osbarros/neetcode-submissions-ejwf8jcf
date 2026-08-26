class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return []

        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        buckets = []
        for n in range(len(nums) + 1):
            buckets.append([])
        
        for n in freq:
            buckets[freq[n]].append(n)

        answer = []

        for i in buckets[::-1]:
            if len(i) != 0:
                for j in range(len(i)):
                    answer.append(i[j])
                    if len(answer) == k:
                        return answer
        