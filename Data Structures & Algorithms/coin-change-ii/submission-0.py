class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for row in dp:
            row[0] = 1


        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                skip = dp[i - 1][j]
                take = 0
                if j - coins[i - 1] >= 0:
                    take = dp[i][j - coins[i - 1]]

                dp[i][j] = skip + take
        
        return dp[-1][-1]