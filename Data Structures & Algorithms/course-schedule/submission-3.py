class Solution:

    def dfs(self, course, visited, path, topSort, courses):

        if course in path:
            self.isFinishable = False
        if course in visited:
            return 
        path.add(course)    
        visited.add(course)


        for c in range(len(courses[course])):
            self.dfs(courses[course][c], visited, path, topSort, courses)
        path.remove(course)
        topSort.append(course)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for prereq in prerequisites:
            courses[prereq[1]].append(prereq[0])
        
        topSort = []
        visited = set()
        path = set()
        self.isFinishable = True

        for i in range(numCourses):
            self.dfs(i, visited, path,topSort, courses)
            
        return self.isFinishable