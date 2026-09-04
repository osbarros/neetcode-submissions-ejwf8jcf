class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numRows = len(obstacleGrid)
        numColumns = len(obstacleGrid[0])

        prevRow = [0 for _ in range(numColumns)]
        for i in range(numRows - 1, -1, -1):
            curRow = [0 for _ in range(numColumns)]
            if i == numRows - 1 and obstacleGrid[i][numColumns - 1] == 0:
                curRow[numColumns - 1] = 1
            elif obstacleGrid[i][numColumns - 1] == 1:
                curRow[numColumns - 1] = 0
            else:
                curRow[numColumns - 1] = prevRow[numColumns - 1]
            for j in range(numColumns - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    curRow[j] = prevRow[j] + curRow[j + 1]
                else:
                    curRow[j] = 0

            prevRow = curRow

        return prevRow[0]
                
                