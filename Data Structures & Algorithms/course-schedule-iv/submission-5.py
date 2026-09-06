class Solution:

    def dfs(self, courses, course, courseA, visited):

        if course in visited:
            return
        visited.add(course)

        if course != courseA:
            self.reachable[courseA].add(course)
        
        
        for c in range(len(courses[course])):
            self.dfs(courses,courses[course][c], courseA, visited)
        



    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        courses = defaultdict(list)
        for prereq in prerequisites:
            courses[prereq[0]].append(prereq[1])
        answer = []
        self.reachable = defaultdict(set)
        

        for i in range(numCourses):
            visited = set()
            self.dfs(courses, i, i, visited)

        for querie in queries:
            if querie[1] in self.reachable[querie[0]]:
                answer.append(True)
            else:
                answer.append(False)

        return answer

        
