class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        cache = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        
        def dfs(i: int, j: int) -> int:
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if cache[i][j] != -1:
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dfs(i + 1, j + 1)
                return cache[i][j] 
            
            
            replace = 1 + dfs(i + 1, j + 1)
            delete = 1 + dfs(i + 1, j)
            add = 1 + dfs(i, j + 1)

            cache[i][j] = min(replace, delete, add)
            return cache[i][j]

        return dfs(0, 0)


