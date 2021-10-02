# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.preorderTraversalHelper(root,arr)
        return arr
    def preorderTraversalHelper(self,node,arr):
        if node is None:
            return
        arr.append(node.val)
        if node.left:
            self.preorderTraversalHelper(node.left,arr)
        if node.right:
            self.preorderTraversalHelper(node.right,arr)