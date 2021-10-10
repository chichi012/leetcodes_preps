# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return
        paths = []
        runningSum = 0
        self.pathSumHelper(root,[],runningSum,paths,targetSum)
        return paths
    
    def pathSumHelper(self,node,ls,runningSum,paths,targetSum):
        if node:
            if not node.left and not node.right:
                runningSum+=node.val
                if runningSum == targetSum:
                    ls.append(node.val)
                    paths.append(ls)
                    return
            if node.left:
                self.pathSumHelper(node.left,ls+[node.val],runningSum+node.val,paths,targetSum)
            if node.right:
                self.pathSumHelper(node.right,ls+[node.val],runningSum+node.val,paths,targetSum)
        

        
        
        
        """DFS SOLUTION"""
        
#         if not root:
#             return
#         paths = []
#         runningSum = 0
#         self.pathSumHelper(root,[],paths,targetSum)
        
#         return paths
    
#     def pathSumHelper(self,node,ls,paths,targetSum):
#         if node:
#             if not node.left and not node.right and targetSum == node.val:
#                 ls.append(node.val)
#                 paths.append(ls)
#             self.pathSumHelper(node.left,ls+[node.val],paths,targetSum-node.val)
#             self.pathSumHelper(node.right, ls+[node.val],paths,targetSum-node.val)
            
            
            
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return
#         paths = []
#         ls = []
#         runningSum = 0
#         self.pathSumHelper(root,ls,paths,runningSum,targetSum)
        
#         return paths
    
#     def pathSumHelper(self,node,ls,paths,runningSum,targetSum):
#         if not node.left and not node.right:
#             runningSum+=node.val
#             if runningSum == targetSum:
#                 ls.append(node.val)
#                 paths.append(ls)
#                 return
#             elif runningSum != targetSum:
#                 break
#         if node.left:
#             ls.append(node.val)
#             self.pathSumHelper(node.left,ls,paths,runningSum+node.val,targetSum)
#         if node.right:
#             ls.append(node.val)
#             self.pathSumHelper(node.right,ls,paths,runningSum+node.val,targetSum)
        