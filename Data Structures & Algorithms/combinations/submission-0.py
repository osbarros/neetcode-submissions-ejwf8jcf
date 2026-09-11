class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        curComb = []

        def helper(i, curComb, combinations, n, k):
            if len(curComb) == k:
                combinations.append(curComb.copy())
                return

            if i > n:
                return
            
            curComb.append(i)
            helper(i + 1, curComb, combinations, n, k)
            curComb.pop()
            helper(i + 1, curComb, combinations, n, k)

        helper(1, curComb, combinations, n, k)
        return combinations

        