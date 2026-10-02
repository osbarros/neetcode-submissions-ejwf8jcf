class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        half = int(totalSum / 2)
        dp = [False for _ in range(half + 1)]
        dp[0] = True

        
        for stone in stones:
            for i in range(len(dp) -1, -1, -1):
                skip = dp[i]
                take = False
                if i - stone >= 0:
                    take = dp[i - stone]
                dp[i] = skip or take
        
        closestToHalf = 0

        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                closestToHalf = i
                break

        return totalSum - (2 * i)
