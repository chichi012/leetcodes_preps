# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        """one line solution"""
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        
        
        
        
        
        
        
        
        
        
        """RECURSIVE SOLUTION"""
#         arr = []
#         self.inorderTraversalHelper(root,arr)
#         return arr
        
#     def inorderTraversalHelper(self,node,arr):
#         if node is None: #empty tree
#             return
#         else:
#             if node.left is not None:
#                 self.inorderTraversalHelper(node.left,arr)
#             arr.append(node.val)
#             if node.right is not None:
#                 self.inorderTraversalHelper(node.right,arr)
            
        
        """USING A STACK"""
        
#         if root is None: #empty tree
#             return None
#         elif root.left is None and root.right is None: #single node tree
#             return [root.val]
#         else:
#             stack = []
#             res = []
#             curr = root
#             while curr is not None or len(stack) >0:
#                 while curr is not None:
#                     stack.append(curr)
#                     curr = curr.left
                
#                 curr = stack.pop()
#                 res.append(curr.val)
#                 curr = curr.right
                
#             return res
            
 