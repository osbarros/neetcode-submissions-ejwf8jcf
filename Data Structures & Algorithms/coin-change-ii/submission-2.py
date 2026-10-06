class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1


        for coin in coins:
            for curAmount in range(amount + 1):
                skip = dp[curAmount]
                take = 0
                if curAmount - coin >= 0:
                    take = dp[curAmount - coin]

                dp[curAmount] = skip + take
        
        return dp[-1]