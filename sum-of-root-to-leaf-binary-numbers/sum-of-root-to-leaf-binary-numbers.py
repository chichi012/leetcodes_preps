# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        """Approach 1: Iterative Preorder Traversal.
        solution using a stack
        
        time complexity: O(N) where NN is a number of nodes, since one has to visit each node.
        Space complexity: up to O(H) to keep the stack, where H is a tree height.
        
        """
        if root is None:
            return
        sums = 0
        stack = [(root,0)]
        
        while stack:
            node,curr_num = stack.pop()
            if node:
                curr_num = curr_num << 1 | node.val

                if not node.left and not node.right:
                    # ie a leaf node, i want to compute my sum
                    sums += curr_num

            #since i'm keeping a pre-order, append right node inside stack first so left gets popped first
                stack.append((node.right,curr_num))
                stack.append((node.left,curr_num))
                
        return sums
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """this just prints out the paths---not a solution"""
#         if not root:
#             return
#         result = []
#         queue = collections.deque([(root,[])])
#         while queue:
#             node,ls = queue.popleft()
            
#             if not node.left and not node.right:
#                 result.append(ls+[node.val])
                
#             if node.left:
#                 queue.append((node.left,ls+[node.val]))
                
#             if node.right:
#                 queue.append((node.right,ls+[node.val]))
                
#         return result 