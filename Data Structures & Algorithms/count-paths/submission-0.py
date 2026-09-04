class Solution:
    def memoization(self, r, c, rows, columns, cache):
        if r == rows or c == columns:
            return 0
        
        if r == rows - 1 and c == columns - 1:
            return 1
        
        if cache[r][c] > 0:
            return cache[r][c]

        cache[r][c] = self.memoization(r + 1, c, rows, columns, cache) + self.memoization(r, c + 1, rows, columns, cache)

        return cache[r][c]

    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)] for _ in range(m)]
        return self.memoization(0, 0, m, n, cache)
        
