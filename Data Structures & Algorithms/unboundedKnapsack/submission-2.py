class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        curRow = [0 for _ in range(capacity + 1)]
        
        for i in range(len(curRow)):
            curRow[i] = i//weight[0] * profit[0]

        prevRow = curRow.copy()

        
        for j in range(1, len(profit)):
            for k in range(capacity + 1):
                skip = prevRow[k]
                include = 0
                if k - weight[j] >= 0:
                    include = profit[j] + curRow[k - weight[j]]
                curRow[k] = max(skip, include)
            
            prevRow = curRow.copy()
        return curRow[capacity]