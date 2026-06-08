class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        deqStudents = deque(students)
        deqSand = deque(sandwiches)

        while count < len(deqStudents):
            if deqStudents[0] == deqSand[0]:
                deqStudents.popleft()
                deqSand.popleft()
                count = 0
            else:
                s = deqStudents.popleft()
                deqStudents.append(s)
                count += 1

        return len(deqStudents)