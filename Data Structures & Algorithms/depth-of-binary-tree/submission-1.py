# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helperDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depthLeft = 1 + self.helperDFS(root.left)
        depthRight = 1 + self.helperDFS(root.right)

        depth = max(depthLeft, depthRight)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helperDFS(root)