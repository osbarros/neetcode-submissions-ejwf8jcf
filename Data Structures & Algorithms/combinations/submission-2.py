class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb = []
        combinations = []

        def helper(curComb, combinations, i, n, k):
            if len(curComb) == k:
                combinations.append(curComb.copy())

            if i > n: 
                return
            
            for j in range(i, n + 1, 1):
                curComb.append(j)
                helper(curComb, combinations, j + 1, n, k)
                curComb.pop()
        
        helper(curComb, combinations, 1, n, k)
        return combinations
