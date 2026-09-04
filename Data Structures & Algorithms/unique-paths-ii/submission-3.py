class Solution:
    def bruteForce(self, r, c, rows, columns, obstacleGrid, cache):
        if r == rows or c == columns or obstacleGrid[r][c] == 1:
            return 0
        
        elif r == rows - 1 and c == columns - 1:
            return 1
        
        elif cache[r][c] > 0:
            return cache[r][c]

        cache[r][c] = self.bruteForce(r + 1, c, rows, columns, obstacleGrid, cache) + self.bruteForce(r, c + 1, rows, columns, obstacleGrid, cache)

        return cache[r][c]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        return self.bruteForce(0,0,len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid, cache)

        