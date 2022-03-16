# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1. if both p and q are greater than current node, go right. 
        2. if both p and q are less than current node, go left
        3. otherwise, if p > current node or q > current node or vise versa, return current node since its the node at the split
        """
        #run time complexity: Worst case O(n) if it is skewed
        #                     Average case O(log N)
        #space complexity: O(1)
        cur = root
        
        while cur: #we are guaranteed to find p and q in the tree according to input conditions
            if p.val > cur.val and q.val > cur.val:
                #go right
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                #go left
                cur = cur.left
            else: #if (p==cur or q == current) or (p <currentnode and q > currentnode) or any other combo, the node at the split is what we want
                return cur
            
                
                