# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return
    
        given_range = [i for i in range(low,high+1)]
        #using a BFS
        queue = [root]
        arr = []
        
        while len(queue) > 0:
            popped = queue.pop(0)
            arr.append(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        sums = 0 
        for i in arr:
            if i in given_range:
                sums+= i
        return sums
      
        