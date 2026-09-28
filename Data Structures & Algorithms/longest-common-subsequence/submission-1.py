class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def dfs(i1: int, i2: int):

            if i1 > len(text1) - 1 or i2 > len(text2) - 1:
                return 0
            
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            
            elif text1[i1] == text2[i2]:
                cache[i1][i2] = 1 + dfs(i1 + 1, i2 + 1)
            
            else: 
                cache[i1][i2] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

            return cache[i1][i2]

        
        return dfs(0, 0)