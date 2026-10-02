class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        half = int(totalSum / 2)
        dp = [[False for _ in range(half + 1)] for _ in range(len(stones) + 1)]

        for x in range(len(stones) + 1):
            dp[x][0] = True

        
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                skip = dp[i - 1][j]
                take = skip
                if j >= stones[i - 1]:
                    take = dp[i - 1][j - stones[i - 1]]
                dp[i][j] = skip or take

        closestToHalf = 0        
        lastColumn = dp[len(stones)]
        for k in range(half, -1, -1):
            if lastColumn[k]:
                closestToHalf = k
                break
        return totalSum - 2 * closestToHalf