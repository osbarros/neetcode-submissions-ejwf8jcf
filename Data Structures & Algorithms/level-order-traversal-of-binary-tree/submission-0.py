# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        answer = []
        queue.append(root)
        currLevelQueue = []
    
        while len(queue) > 0:
            currLevelQueue = []
            for i in range(len(queue)):
                curr = queue.popleft()
                currLevelQueue.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            answer.append(currLevelQueue)
        return answer
                
        

            
    