class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque()
        count = 0

        while count < len(students):
            if not students:
                return 0
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                s = students.pop(0)
                students.append(s)
                count += 1


        print(students)
        print(sandwiches)
        return len(students)