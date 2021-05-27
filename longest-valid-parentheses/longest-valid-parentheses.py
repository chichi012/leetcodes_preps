class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i,char in enumerate(s):
            #check if char is open or closed parenthesis
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curlen =  i - stack[-1]
                    max_len = max(max_len,curlen)
        return max_len
        
        
#GET AHEAD CODE
'''
        stack = []
        max_len = 0
        for i,char in enumerate(s):
            #check if char is open or closed parenthesis
            if char == '(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    curlen =  i - stack.pop() + 1
                    max_len = max(max_len,curlen)
                else:
                    pass
        return max_len
        '''
