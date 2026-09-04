class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        if k < len(points):

            
            for i in range(k):
                x = points[i][0]
                y = points[i][1]
                distance = ((x)**2 + (y)**2)**0.5
                heap.append((-distance,x, y))
            heapq.heapify(heap)
            
            for j in range(k, len(points)):
                x = points[j][0]
                y = points[j][1]
                distance = ((x)**2 + (y)**2)**0.5
                if distance < abs(heap[0][0]):
                    heapq.heapreplace(heap,(-distance, x, y))

        else:
            for z in range(len(points)):
                x = points[z][0]
                y = points[z][1]
                distance = ((x)**2 + (y)**2)**0.5
                heapq.heappush(heap,(-distance, x, y))

        answer = [tupla[1:] for tupla in heap]
        return answer
