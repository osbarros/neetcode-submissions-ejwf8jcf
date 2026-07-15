class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        if k < len(nums):
            for i in range(k):
                heapq.heappush(self.heap, nums[i])

            for j in range(k, len(nums)):
                if nums[j] > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, nums[j])

        else:
            for k in range(len(nums)):
                heapq.heappush(self.heap, nums[k])
            

    def add(self, val: int) -> int:
        if not self.heap:
            heapq.heappush(self.heap, val)
            return val

        if val > self.heap[0]:
            if len(self.heap) == self.k:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
