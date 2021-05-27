import collections
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        heights.append(0)
        h_stack = collections.deque()
        p_stack = collections.deque()
        
        for i in range(len(heights)):
            lastwidth = len(heights)+1
            while len(h_stack)!= 0 and h_stack[-1] > heights[i]:
                lastwidth = p_stack[-1]
                ind1 = p_stack.pop()
                ind2 = h_stack.pop()
                curarea = (i - ind1) * ind2
                if max_area < curarea:
                    max_area = curarea
                    indices = (ind1,i-1)
            
            if len(h_stack)==0 or h_stack[-1] < heights[i]:
                h_stack.append(heights[i])
                p_stack.append(min(lastwidth,i))
        return max_area
        