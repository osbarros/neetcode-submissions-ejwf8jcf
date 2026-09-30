class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        capacity1D = [0 for _ in range(capacity + 1)]
        
        for i in range(len(profit)):
            for j in range(capacity + 1):
                if weight[i] <= j:
                    capacity1D[j] = max(capacity1D[j], profit[i] + capacity1D[j - weight[i]])

        return capacity1D[-1]