class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prevRow = [float("inf") for _ in range(amount + 1)]
        prevRow[0] = 0

        for i in range(len(coins)):
            curRow = [float("inf") for _ in range(amount + 1)]
            curRow[0] = 0
            for j in range(amount + 1):
                skip = prevRow[j]
                take = skip
                if j - coins[i]>= 0:
                    take = 1 + curRow[j - coins[i]]
                curRow[j] = min(skip, take)
            prevRow = curRow

        return curRow[-1] if curRow[-1] != float("inf") else -1
        
            