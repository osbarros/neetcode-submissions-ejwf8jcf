class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        duration = 0
        queue = deque()
        freshFruitCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruitCount += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if freshFruitCount == 0:
            return 0
        elif len(queue) == 0:
            return -1



        while len(queue) > 0:
            if freshFruitCount == 0:
                    return duration
            duration += 1
            for k in range(len(queue)):
                r, c = queue.popleft()

                if (r + 1 < len(grid) and grid[r  + 1][c] == 1):
                    queue.append((r + 1, c))
                    grid[r + 1][c] = 2
                    freshFruitCount -= 1


                if (r - 1 >= 0 and grid[r  - 1][c] == 1):
                    queue.append((r - 1, c))
                    grid[r - 1][c] = 2
                    freshFruitCount -= 1

                if (c + 1 < len(grid[0]) and grid[r][c + 1] == 1):
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2
                    freshFruitCount -= 1

                if (c - 1 >= 0 and grid[r][c - 1] == 1):
                    queue.append((r, c - 1))
                    grid[r][c - 1] = 2
                    freshFruitCount -= 1


        return -1


    



        