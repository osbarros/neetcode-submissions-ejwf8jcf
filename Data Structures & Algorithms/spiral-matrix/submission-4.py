class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        firstRow = 0
        lastColumn = len(matrix[0]) - 1
        lastRow = len(matrix) - 1
        firstColumn = 0


        while firstRow <= lastRow and firstColumn <= lastColumn:
            for i in range(firstColumn, lastColumn + 1):
                spiral.append(matrix[firstRow][i])
            
            firstRow += 1
            
            for j in range(firstRow, lastRow + 1):
                spiral.append(matrix[j][lastColumn])

            lastColumn -= 1

            if firstRow <= lastRow:
                for k in range(lastColumn, firstColumn - 1, -1):
                    spiral.append(matrix[lastRow][k])
                lastRow -= 1

            if firstColumn <= lastColumn:
                for z in range(lastRow, firstRow - 1, -1):
                    spiral.append(matrix[z][firstColumn])
                firstColumn += 1

            print(spiral)  
        
        return spiral

        

        



        