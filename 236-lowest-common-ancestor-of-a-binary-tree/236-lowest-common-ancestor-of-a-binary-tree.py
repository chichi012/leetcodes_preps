# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        """
        Using Depth First Search Algorithm, Once we reach the desired nodes p and q, we can backtrack and find the lowest common ancestor.
        
        Complexity Analysis

Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.
        """
        self.result = None

    
        def lowestCommonAncestorHelper(node):
            if not node:
                return 0

            left = lowestCommonAncestorHelper(node.left)

            right = lowestCommonAncestorHelper(node.right)
    
            if node == p or node == q:
                mid = 1 
            else:
                mid = 0
            
            
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.result = node
                
            # Return True if either of the three bool values is True.
            return mid or left or right
                
        #recurse tree    
        lowestCommonAncestorHelper(root)
        return self.result
            
            
