class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)]for _ in range(m + 1)]

        count0 = defaultdict(int)
        count1 = defaultdict(int)
        for s in strs:
            count0[s] = s.count('0')
            count1[s] = s.count('1')


        for s in strs: 
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= count0[s] and j >= count1[s]:
                        dp[i][j] = max(dp[i][j], 1 + dp[i - count0[s]][j - count1[s]])

        return dp[m][n]



