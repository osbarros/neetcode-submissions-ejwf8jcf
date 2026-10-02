class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        half = totalSum / 2 

        cache = [[-1 for _ in range(totalSum)] for _ in range(len(stones))]

        def dfs(i: int, currentSum: int):

            if i == len(stones):
                return currentSum

            if cache[i][currentSum] != -1:
                return cache[i][currentSum]
            
            skip = dfs(i + 1, currentSum)
            take = dfs(i + 1, currentSum + stones[i])

            if abs(skip - half) <= abs(take - half):
                cache[i][currentSum] = skip
            else:
                cache[i][currentSum] = take
            return cache[i][currentSum]

        return abs(totalSum - 2 * dfs(0, 0))