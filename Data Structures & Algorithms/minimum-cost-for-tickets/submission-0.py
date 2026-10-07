class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = [-1 for _ in range(len(days))]
        def binarySearch(days: List[int], targetDay: int):
            high = len(days) - 1
            low = 0
            
            while high >= low:
                mid = (high + low) // 2

                if targetDay == days[mid]:
                    return mid
                
                elif targetDay < days[mid]:
                    high = mid - 1
                
                else: 
                    low = mid + 1

            return low

        def dfs(index: int) -> int:

            if index == len(days):
                return 0

            if cache[index] != -1:
                return cache[index]
        
            ticket1Day = costs[0] + dfs(binarySearch(days, days[index] + 1)) 
            ticket7Days = costs[1] + dfs(binarySearch(days, days[index] + 7))
            ticket30Days = costs[2] + dfs(binarySearch(days, days[index] + 30))

            cache[index] = min(ticket1Day, ticket7Days, ticket30Days)
            return cache[index]

        return dfs(0)
    



            

        