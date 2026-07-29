class Solution:

    def dfs(self, root):
        if root in self.visited:
            self.isFinishable = False
        elif self.isFinishable and root not in self.validated:
            self.visited.add(root)
            if root in self.graph and self.graph[root]:
                for neighbor in self.graph[root]:
                    self.dfs(neighbor)
            self.visited.remove(root)
            if self.isFinishable: 
                self.validated.add(root)
            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        for prereq in prerequisites:
            if prereq[1] not in self.graph:
                self.graph[prereq[1]] = [prereq[0]]
            else:
                self.graph[prereq[1]].append(prereq[0])
            
        self.visited = set()
        self.validated = set()
        self.isFinishable = True

        for i in range(numCourses):
            if i not in self.validated and self.isFinishable:
                self.dfs(i)

        return self.isFinishable



             