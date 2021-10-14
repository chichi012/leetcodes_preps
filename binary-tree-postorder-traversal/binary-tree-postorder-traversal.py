# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right)+ [root.val] if root else []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """for postorder, the last node in the result is always the root node
        link to solution: https://youtu.be/B6XTLPpsW7k 
        left > right > node
        
        RECURSIVE SOLUTION
        """
#         arr = []
#         self.postorderTraversalHelper(root,arr)
#         return arr
        
#     def postorderTraversalHelper(self,node,arr):
#         if node is None:
#             return
# #        left > right > node
#         if node.left:
#             self.postorderTraversalHelper(node.left,arr)
#         if node.right:
#             self.postorderTraversalHelper(node.right,arr)
#         if node:
#             arr.append(node.val)
        
        



#        arr = []
#         self.postorderTraversalHelper(root,arr)
#         return arr
        
#     def postorderTraversalHelper(self,node,arr):
#         if node is None:
#             return
#        left > right > node
#       l = self.postorderTraversalHelper(node.left,arr)
#         if l is not None:
#             arr.append(l.val)
#         r = self.postorderTraversalHelper(node.right,arr)
#         if r is not None:
#             arr.append(r.val)
#         arr.append(node.val)
        
        
    
        
        
        """Using a STACK and keeping a boolean..mark True only when we've visited its children"""
        # arr = []
        # stack = [(root,False)]
        # while len(stack) > 0:
        #     node,visited = stack.pop()
        #     if node:
        #         if visited:
        #             arr.append(node.val)
        #         else:
        #             stack.append((node,True))
        #             stack.append((node.right,False))
        #             stack.append((node.left,False))
        # return arr