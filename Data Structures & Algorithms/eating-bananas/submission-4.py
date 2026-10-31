class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxK = max(piles)
        minK = max(1, sum(piles)// h)


        L = minK
        R = maxK
        
        def isPossibleToEatAllBananas(piles: List[int], k: int, h) -> bool:

            count = 0
            for p in piles:
                count += math.ceil(p / k)

            return count <= h
                    
            
        bestRate = maxK

        while (L <= R):
            mid = (L + R) // 2
            
            if isPossibleToEatAllBananas(piles, mid, h):
                bestRate = min(mid, bestRate)
                R = mid - 1
    

            else:
                L = mid + 1

        return bestRate







