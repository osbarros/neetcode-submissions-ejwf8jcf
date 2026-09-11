class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for time in times:
            adjList[time[0]].append((time[1], time[2]))
        
        minHeap = [(0, k)]
        shortest = {}

        while minHeap and len(shortest) < n:
            time, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = time

            for node2, time2 in adjList[node]:
                heapq.heappush(minHeap, (time + time2, node2))
             
        
        if len(shortest) != n:
            return -1
        return max(shortest.values())
                