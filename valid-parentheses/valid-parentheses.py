import collections
class Solution:
    def isValid(self, s: str) -> bool:
        valid_parenthesis = {')':'(', '}':'{',']':'['}
        stack_s = []
      
    #Input: s = "{[]}""
        for char in s:
            if char in valid_parenthesis.values():
                stack_s.append(char)
            elif char in valid_parenthesis.keys():
                if len(stack_s) == 0 or valid_parenthesis[char]!= stack_s.pop():
                    return False
        return stack_s == []
            
                    
                
        