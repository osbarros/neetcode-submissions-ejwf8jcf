# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        answer = []

        if not root:
            return []

        while queue:
            lenQueue = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == lenQueue - 1:
                    answer.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return answer