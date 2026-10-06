class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1


        for coin in coins:
            for curAmount in range(coin, amount + 1):
                dp[curAmount] += dp[curAmount - coin]
        
        return dp[-1]