# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        if root.left is None and root.right is None:
            return 0
        self.sums = 0
        isLeft = False
        self.sumOfLeftLeavesHelper(root,isLeft)
        return self.sums
    
    def sumOfLeftLeavesHelper(self,node,isLeft):
        if isLeft and node.left is None and node.right is None:
            #this specifies its a leaf node
            self.sums+= node.val
            return self.sums
        if node.left:
            self.sumOfLeftLeavesHelper(node.left, True)
        if node.right:       
            self.sumOfLeftLeavesHelper(node.right, False)
            