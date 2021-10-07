# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 
        runningSum = 0
        sumsList =[]
        self.hasPathSumHelper(root,runningSum,sumsList,targetSum)
        return True if targetSum in sumsList else False
    
    def hasPathSumHelper(self,node,runningSum,sumsList,targetSum):
        
        if not node.left and not node.right:
            sumsList.append(runningSum+ node.val)
            # print(sumsList)
            return sumsList
        if node.left:
            self.hasPathSumHelper(node.left,runningSum+ node.val,sumsList,targetSum)       
        if node.right:
            self.hasPathSumHelper(node.right,runningSum+ node.val,sumsList,targetSum)
            
            
        
        