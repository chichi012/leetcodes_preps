# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        """
        Using Depth First Search Algorithm
        
        """
        self.result = None
    
        def lowestCommonAncestorHelper(node):
            if not node:
                return False

            # if node.val == p.val or node.val == q.val:
            #     return result
            # result = node
            # node = node.left
            left = lowestCommonAncestorHelper(node.left)

#             if node.right:
#                 result = node
#                 node = node.right
            right = lowestCommonAncestorHelper(node.right)
    
            mid = node == p or node == q
            
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.result = node
                
            # Return True if either of the three bool values is True.
            return mid or left or right
                
        #recurse tree    
        lowestCommonAncestorHelper(root)
        return self.result
            
            
