# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #O(N) time and O(1) space. Takes longer time to run
        
#         get to half
#         reverse last half
#         iterate from beginning and last half if both are equal else not a palindrome
#         iter1 = head
#         iter2 = head
#         while iter2.next and iter2.next.next:
#             iter1 = iter1.next
#             iter2 = iter2.next.next
            
#         new_list = iter1.next #starts second list
#         iter1.next = None #ends list of head at firsthalf
        
        
#         #reverse last half
#         iter1 = new_list
#         temp = None
#         prev = None
        
#         while iter1:
#             temp = iter1.next 
#             iter1.next = prev
#             prev = iter1
#             iter1 = temp
        
        
#         # iterate from beginning and last half if both are equal else not a palindrome
#         a = head
#         b = prev
#         while b:
#             if b.val != a.val:
#                 return False
#             a = a.next
#             b = b.next
#         return True
            
        
        # #O(N) time and O(N) space. Takes Shorter time to run but more space
    # """SOLUTION USING RECURSION 
    # keep a pointer at fake node with its .next = head, recurse through linkedlist to end....on returns, compare returned value with moving pointer at head..return true if same"""
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = ListNode()
        start.next = head;
        iter1 = head
        result = self.isPalindromeHelper(start,iter1)
        return result
        
    
    def isPalindromeHelper(self,start,iter1):
        if iter1 is None:
            return True
        else:
            result = self.isPalindromeHelper(start,iter1.next)
            if result == False or iter1.val != start.next.val:
                return False
            else:
                start.next = start.next.next
                return True
    
    
                
    

