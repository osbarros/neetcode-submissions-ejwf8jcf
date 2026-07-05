# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperDFS(self, root: Optional[TreeNode], inorderList: List[int]):
        if not root:
            return 
        self.helperDFS(root.left, inorderList)
        inorderList.append(root.val)
        self.helperDFS(root.right, inorderList)

        return inorderList
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        inorderList = []


        if not root:
            return inorderList

        self.helperDFS(root, inorderList)

        return inorderList
