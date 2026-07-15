class Solution:

    def markAsVisited(self, grid: List[List[str]], nr, nc):
        self.visited.add((nr, nc))
        
        if (nr + 1 <= (len(grid) -1)) and grid[nr + 1][nc] == "1" and (nr + 1, nc) not in self.visited:
            self.markAsVisited(grid, nr + 1, nc)
        if (nc + 1 <= (len(grid[0]) -1)) and grid[nr][nc + 1] == "1" and (nr, nc + 1) not in self.visited:
            self.markAsVisited(grid, nr, nc + 1)
        if (nr - 1 >= 0) and grid[nr - 1][nc] == "1" and (nr - 1, nc) not in self.visited:
            self.markAsVisited(grid, nr - 1, nc)
        if (nc - 1 >= 0) and grid[nr][nc - 1] == "1" and (nr, nc - 1) not in self.visited:
            self.markAsVisited(grid, nr, nc - 1) 
        

    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.count += 1
                    self.markAsVisited(grid, i, j)

        return self.count
        

