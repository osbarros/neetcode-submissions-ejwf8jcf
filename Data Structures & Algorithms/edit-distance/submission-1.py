class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0: 
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else: 
                    replace =  1 + dp[i - 1][j - 1]
                    add = 1 + dp[i][j - 1]
                    remove = 1 + dp[i - 1][j]
                    dp[i][j] = min(replace, add, remove)

        return dp[-1][-1] 
                

                