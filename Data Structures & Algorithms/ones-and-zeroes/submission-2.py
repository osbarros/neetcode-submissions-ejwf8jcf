class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]

        count0 = defaultdict(int)
        count1 = defaultdict(int)
        for i in range(len(strs)):
            count0[i] = strs[i].count('0')
            count1[i] = strs[i].count('1') 

        def dfs(i, zerosLeft, onesLeft):
            if i == len(strs):
                return 0

            if cache[i][zerosLeft][onesLeft] != -1:
                return cache[i][zerosLeft][onesLeft]

            else:
                skip = dfs(i + 1, zerosLeft, onesLeft)
                take = skip
                
                if count0[i] <= zerosLeft and count1[i] <= onesLeft:
                    take = 1 + dfs(i + 1, zerosLeft - count0[i], onesLeft - count1[i])
                
                cache[i][zerosLeft][onesLeft] = max(skip, take)
                
                return cache[i][zerosLeft][onesLeft]
            
        return dfs(0, m, n)
            
