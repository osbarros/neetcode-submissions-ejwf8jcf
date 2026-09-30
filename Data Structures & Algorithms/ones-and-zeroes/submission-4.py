class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        prevMatrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        curMatrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        count0 = defaultdict(int)
        count1 = defaultdict(int)
        for s in strs:
            count0[s] = s.count('0')
            count1[s] = s.count('1')
        
        for i in range(m + 1):
            for j in range(n + 1):
                if count0[strs[0]] <= i and count1[strs[0]] <= j:
                    prevMatrix[i][j] = 1
        

        for k in range(1, len(strs)):
            curMatrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    skip = prevMatrix[i][j]
                    take = skip
                    if count0[strs[k]] <= i and count1[strs[k]] <= j:
                        take = 1 + prevMatrix[i - count0[strs[k]]][j - count1[strs[k]]]
                    curMatrix[i][j] = max(skip, take)
            prevMatrix = curMatrix
            

        return curMatrix[m][n]




