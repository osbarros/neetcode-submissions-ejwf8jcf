class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid) - 1][len(grid[0]) - 1]:
            return -1
        distance = 0
        queue = deque()
        visited = set()

        queue.append((0, 0))

        

        while len(queue) > 0:
            distance += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 1 or (r,c) in visited:
                    continue

                visited.add((r, c))
                
                
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return distance

                
            
                queue.append((r + 1, c))
            
            
                queue.append((r - 1, c))
            
            
                queue.append((r, c + 1))
            
            
                queue.append((r, c - 1))

            
                queue.append((r + 1, c + 1))

            
                queue.append((r - 1, c - 1))
            
            
                queue.append((r - 1, c + 1))

            
                queue.append((r + 1, c - 1))

        return -1

                
                