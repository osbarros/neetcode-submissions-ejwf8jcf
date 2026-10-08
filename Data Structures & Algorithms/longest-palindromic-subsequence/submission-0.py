class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(L: int, R: int) -> int:
            
            if L > R:
                return 0
            if L == R:
                return 1

            if (L, R) in cache:
                return cache[(L, R)]
            
            if s[L] == s[R]:
                cache[(L, R)] =  2 + dfs(L + 1, R - 1)
                return cache[(L, R)]
            
            cache[(L, R)] = max(dfs(L, R - 1), dfs(L + 1, R))
            return cache[(L, R)]

        return dfs(0, len(s) - 1)