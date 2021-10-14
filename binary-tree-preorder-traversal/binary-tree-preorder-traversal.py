# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """one line solution"""
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
                
#         """ITERATIVE SOLUTION 2"""
#         stack = [root]
#         res = []

#         while len(stack) > 0: 
#             curr = stack.pop()
#             if curr is not None:
#                 res.append(curr.val)
#                 stack.append(curr.right)
#                 stack.append(curr.left)
#         return res
            
        

        
        """ITERATIVE SOLUTION 1"""
#         stack = []
#         res = []
#         curr = root
#         while curr is not None or len(stack) > 0:   
#             while curr is not None:
#                 res.append(curr.val)
#                 stack.append(curr)
#                 curr = curr.left
            
#             curr = stack.pop()
#             curr = curr.right
            
#         return res
            
        

        
        """RECURSIVE SOLUTION"""
        
    #     arr = []
    #     self.preorderTraversalHelper(root,arr)
    #     return arr
    # def preorderTraversalHelper(self,node,arr):
    #     if node is None:
    #         return
    #     arr.append(node.val)
    #     if node.left:
    #         self.preorderTraversalHelper(node.left,arr)
    #     if node.right:
    #         self.preorderTraversalHelper(node.right,arr)