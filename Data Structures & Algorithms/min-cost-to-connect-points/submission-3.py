class UnionFind:
    def __init__(self, numEdges):
        self.rank = {}
        self.parents = {}

        for i in range(numEdges):
            self.rank[i] = 0
            self.parents[i] = i

    def find(self, edge1):
        parent = self.parents[edge1]
        while parent != self.parents[parent]:
            parent = self.parents[parent]
        return parent
    
    def union(self, edge1, edge2):
        parent1 = self.find(edge1)
        parent2 = self.find(edge2)

        if parent1 == parent2:
            return False
        
        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += 1
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        totalCost = 0
        minHeap = []
        mst = []
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap,(distance, i, j))
        unionFind = UnionFind(len(points))

        while len(mst) < len(points) - 1:
            distance, origin, dest = heapq.heappop(minHeap)
            if not unionFind.union(origin, dest):
                continue
            mst.append((origin, dest))
            totalCost += distance
        
        return totalCost

        


        