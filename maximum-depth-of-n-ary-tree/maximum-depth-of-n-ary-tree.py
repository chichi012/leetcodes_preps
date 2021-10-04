"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node',depth = 0) -> int:
        if root is None:
            return 0
        
        depth = 0

        for child in root.children:
            if child:
                depth = max(depth,self.maxDepth(child,depth+1))
            
        return 1+depth
        