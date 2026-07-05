# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        heightLeft = self.helper(root.left)
        heightRight = self.helper(root.right)

        height = 1 + max(heightLeft, heightRight)

        if abs(heightLeft - heightRight) > 1:
            self.balanced = False
        
        return height


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if not root:
            return True
        
        self.helper(root)

        return self.balanced