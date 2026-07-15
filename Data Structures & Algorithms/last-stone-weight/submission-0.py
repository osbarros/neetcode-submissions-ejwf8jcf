class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxWeightHeap = [-stone for stone in stones]
        heapq.heapify(maxWeightHeap)

        while len(maxWeightHeap) > 1:
            y = heapq.heappop(maxWeightHeap)
            x = heapq.heappop(maxWeightHeap)


            if abs(y) > abs(x):
                heapq.heappush(maxWeightHeap, y - x)
            
        
        return -maxWeightHeap[0] if maxWeightHeap else 0
        


