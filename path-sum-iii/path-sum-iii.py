# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """SOLUTION USING TWO DFS"""
        if root is None:
            return 0
        self.counter = 0
#         first layer of dfs to go through the node
        self.dfs(root,targetSum)
        return self.counter
        
        
    def dfs(self,node,targetSum):
        # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
        if node is None:
            return
        self.pathSumHelper(node,targetSum)
        self.dfs(node.left,targetSum)
        self.dfs(node.right,targetSum)
        
        #this used the pre-order trasversal. we could have used in-order or post order
        
    def pathSumHelper(self,node,targetSum):
        # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
        if not node:
            return
        if node.val ==targetSum:
            self.counter +=1
        if node.left:
            self.pathSumHelper(node.left,targetSum-node.val)
        if node.right:
            self.pathSumHelper(node.right,targetSum-node.val)
            
   