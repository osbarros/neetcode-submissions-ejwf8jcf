class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for r in range(len(dp)):
            dp[r][0] = 0
        
        for r in range(1, len(coins) + 1):
            for c in range(amount + 1):
                skip = dp[r - 1][c]
                take = skip
                if c - coins[r - 1] >= 0:
                    take = 1 + dp[r][c - coins[r - 1]]
                dp[r][c] = min(skip, take)
            
        output = dp[-1][-1]

        return output if output != float("inf") else -1

        