class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prevRow = [0 for _ in range(amount + 1)]
        prevRow[0] = 1


        for i in range(len(coins)):
            curRow = [0 for _ in range(amount + 1)]
            curRow[0] = 1
            for j in range(amount + 1):
                skip = prevRow[j]
                take = 0
                if j - coins[i - 1] >= 0:
                    take = curRow[j - coins[i - 1]]

                curRow[j] = skip + take
            prevRow = curRow
        
        return prevRow[-1]