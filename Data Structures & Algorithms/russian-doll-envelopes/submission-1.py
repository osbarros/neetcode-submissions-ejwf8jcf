class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def getBisectLeft(value: int, arr: List[int]) -> int:
            L = 0
            R = len(arr)

            while L < R:
                mid = (L + R) // 2
                if arr[mid] < value:
                    L = mid + 1
                else:
                    R = mid 
            return L

        envelopes.sort(key = lambda x: (x[0], -x[1]))
        heights = [envelope[1] for envelope in envelopes]
 
        tails = []

        for height in heights:
            index = getBisectLeft(height, tails)
            if index < len(tails):
                tails[index] = height
            else:
                tails.append(height)

        return len(tails) 

    




                



