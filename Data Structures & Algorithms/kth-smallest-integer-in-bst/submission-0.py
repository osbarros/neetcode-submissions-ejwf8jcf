# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderDFS(self, root: Optional[TreeNode]):

        if not root:
            return 

        if self.answer:
            return
        
        self.inorderDFS(root.left)
        self.count += 1
        if self.count == k:
            self.answer = root.val
        self.inorderDFS(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.answer = None
        self.count = 0
        self.inorderDFS(root)
        return self.answer
        