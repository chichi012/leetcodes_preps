# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode],parentNode = None) -> bool:
        """ITERATIVE METHOD"""
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True      


        
        """RECURSION METHOD"""
#         if root is None:
#             return True
        
#         l = root.left
#         r = root.right
        
#         return self.isSymmetricHelper(l,r)
        



#     def isSymmetricHelper(self,node1,node2):
#         if node1 is None and node2 is None:
#             return True
#         if node1 is None or node2 is None:
#             return False
    
#         if node1.val == node2.val:
#             outpair= self.isSymmetricHelper(node1.left,node2.right)
#             inpair = self.isSymmetricHelper(node1.right,node2.left)
#             return outpair and inpair

        