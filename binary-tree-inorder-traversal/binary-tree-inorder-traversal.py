# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.inorderTraversalHelper(root,arr)
        return arr
        
    def inorderTraversalHelper(self,node,arr):
        if node is None: #empty tree
            return
        else:
            if node.left is not None:
                self.inorderTraversalHelper(node.left,arr)
            arr.append(node.val)
            if node.right is not None:
                self.inorderTraversalHelper(node.right,arr)
            
        
        
        
        
        
        
        
        
        
        
#         if root is None: #empty tree
#             return None
#         elif root.left is None and root.right is None: #single node tree
#             return [root.val]
#         else:
#             queue = [root]
#             arr = []
#             i = 0
#             while i < len(queue):
#                 popped = queue[i]
#                 arr.append(root.val)
#                 i+=1
#                 if popped.left:
#                     queue.append(popped.left)
#                 if popped.right:
#                     queue.append(popped.right.left)
#                     queue.append(popped.right)
                    
#         return arr
                
            
            