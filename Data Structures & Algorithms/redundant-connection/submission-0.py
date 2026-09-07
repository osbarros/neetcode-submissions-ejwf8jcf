class UnionFind:
    def __init__(self, numEdges):
        self.rank = {}
        self.parents = {}
        for i in range(numEdges + 1):
            self.rank[i + 1] = 0
            self.parents[i + 1] = i + 1
    
    def find(self, edge):
        parent = self.parents[edge]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, edge1, edge2):
        parent1, parent2 = self.find(edge1), self.find(edge2)

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            unionFind = UnionFind(len(edges))
            for edge in edges:
                if not unionFind.union(edge[0], edge[1]):
                    return edge
            
        