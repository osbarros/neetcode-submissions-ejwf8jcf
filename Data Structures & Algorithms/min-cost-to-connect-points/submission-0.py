class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0] 
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, distance))
                graph[j].append((i, distance))
        

        minHeap = []
        for neighbor, distance in graph[0]:
            heapq.heappush(minHeap, (distance, neighbor))
        
        visited = {0}
        minCost = 0

        while minHeap and len(visited) <= len(points):
            distance, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            minCost += distance

            for neighbor, distance in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (distance, neighbor))
        
        return minCost
            




