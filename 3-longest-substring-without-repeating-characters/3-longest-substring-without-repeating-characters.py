class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #time complexity: O(N) where N is the length of s
        #space complexity: O(M) where M is the number of unique character in s. If we know its ASCII dict of say 256 characters then  we know we'll be using O(256) space and that is contant space
        
        char_set = set()   #containing only distinct chars we are currently assessing in the window range
        left = 0
        result = 0
        
        for right in range(len(s)):
            #check if element at index str[right] exist in set. if it does, delete the corresponding elemnt at str[left].
            #this is to keep shrinking the sliding window until the duplicate is taken off, then keep increamenting left
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1     #to check if next one too is duplicated
            
            char_set.add(s[right])   #after removing duplicates, go ahead and add the new character
            result = max(result,right-left+1)
            
        return result
        