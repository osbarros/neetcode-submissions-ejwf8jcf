"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque()
        visited = set()
        copies = {}

        rootCopy = None
        queue.append(node)
        while (len(queue) > 0):
            curr = queue.popleft()
            if curr in visited:
                continue
            if curr not in copies:
                currCopy = Node(curr.val)
            else:
                currCopy = copies[curr]
            if not copies:
                rootCopy = currCopy        
            copies[curr] = currCopy
            for neighbor in curr.neighbors:
                if neighbor not in copies:
                    neighborCopy = Node(neighbor.val)
                    copies[neighbor] = neighborCopy
                
                copies[curr].neighbors.append(copies[neighbor])
                queue.append(neighbor)
            visited.add(curr)
        
        return rootCopy
                    
                        
                
                
