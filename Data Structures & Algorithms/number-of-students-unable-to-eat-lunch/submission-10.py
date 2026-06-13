class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_circular = students.count(0)
        count_square = students.count(1)

        for s in sandwiches:
            
            if s == 0:
                if count_circular == 0:
                    return count_square
                
                else: 
                    count_circular -= 1
                
            elif s == 1:
                if count_square == 0:
                    return count_circular
                
                else:
                    count_square -= 1
        
        return 0