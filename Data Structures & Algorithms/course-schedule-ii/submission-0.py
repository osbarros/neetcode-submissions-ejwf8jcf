class Solution:

    def dfs(self, course, visited, path, courses):

        if course in path:
            self.isFinishable = False
            return
        if course in visited:
            return 
        path.add(course)    
        visited.add(course)


        for c in range(len(courses[course])):
            self.dfs(courses[course][c], visited, path, courses)
        path.remove(course)
        self.ordering.append(course)


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        self.isFinishable = True
        self.ordering = []

        #O(E)
        courses = defaultdict(list)
        for prereq in prerequisites:
            courses[prereq[1]].append(prereq[0])

        for i in range(numCourses):
            self.dfs(i, visited, path, courses)
            
        if not self.isFinishable:
            return []
        else:
            self.ordering.reverse()
            return self.ordering

        