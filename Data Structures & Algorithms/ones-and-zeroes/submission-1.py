class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]

        def dfs(strs, cache, i, zerosLeft, onesLeft):
            if i == len(strs):
                return 0

            if cache[i][zerosLeft][onesLeft] != -1:
                return cache[i][zerosLeft][onesLeft]

            else:
                skip = dfs(strs, cache, i + 1, zerosLeft, onesLeft)
                take = skip
                
                if strs[i].count('0') <= zerosLeft and strs[i].count('1') <= onesLeft:
                    take = 1 + dfs(strs, cache, i + 1, zerosLeft - strs[i].count('0'), onesLeft - strs[i].count('1'))
                
                cache[i][zerosLeft][onesLeft] = max(skip, take)
                
                return cache[i][zerosLeft][onesLeft]
            
        return dfs(strs, cache, 0, m, n)
            
