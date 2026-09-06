class Solution:

    def dfs(self, courses, course, courseA, courseB, visited):

        if course in visited:
            return
        visited.add(course)
        
        if course == courseB:
            return True
        
        for c in range(len(courses[course])):
            if self.dfs(courses,courses[course][c], courseA, courseB, visited):
                return True
        
        return False




    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        courses = defaultdict(list)
        for prereq in prerequisites:
            courses[prereq[0]].append(prereq[1])
        answer = []
        

        for querie in queries:
            visited = set()
            if self.dfs(courses, querie[0], querie[0], querie[1], visited):
                answer.append(True)
            else:
                answer.append(False)

        return answer

        
