# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode,ls=None) -> List[str]:
        """DFS + STACK"""
        if not root:
            return
        result = []
        stack = [(root,"")]
        while stack:
            node,string = stack.pop()
            
            if not node.left and not node.right:
                result.append(string+str(node.val))
                
            if node.left:
                stack.append((node.left,string+str(node.val)+"->"))
                
            if node.right:
                stack.append((node.right,string+str(node.val)+ "->"))
                
        return result
                

   








#         if not root:
#             return []
#         ls = []
#         ls.append(str(root.val))
#         if root.left:
#             ls.append(str(root.left.val))
#             self.binaryTreePaths(root.left,ls)
#         if root.right:
#             ls.append(str(root.right.val))
#             self.binaryTreePaths(root.right,ls)
#         return ls
        