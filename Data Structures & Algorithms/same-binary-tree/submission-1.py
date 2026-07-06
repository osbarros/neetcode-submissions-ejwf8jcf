# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q: 
            return True
        elif not p:
            return False
        elif not q:
            return False
        
        elif p.val != q.val:
            return False
        
        else:
            return self.helper(p.left, q.left) and self.helper(p.right, q.right)
            
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
        