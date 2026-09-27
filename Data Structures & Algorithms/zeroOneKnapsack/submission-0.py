class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        curRow = [0 for _ in range(capacity + 1)]
        prevRow = [0 for _ in range(capacity + 1)]
        for i in range(len(curRow)):
            if i >= weight[0]:
                curRow[i] = profit[0]

        
        for j in range(len(profit)):
            for k in range(capacity + 1):
                skip = prevRow[k]
                include = 0
                if k - weight[j] >= 0:
                    include = profit[j] + prevRow[k - weight[j]]
                curRow[k] = max(skip, include)
            
            prevRow = curRow.copy()
        return curRow[capacity]