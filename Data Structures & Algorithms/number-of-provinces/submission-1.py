class Solution:

    def dfsHelper(self, isConnected: List[List[int]], nr: int):
        for i in range(len(isConnected)):
            if isConnected[nr][i] == 1:
                self.visited.add(nr)
                if i not in self.visited:
                    self.dfsHelper(isConnected, i)



    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.count = 0
        self.visited = set()
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.count += 1
                self.dfsHelper(isConnected, i)

        return self.count

