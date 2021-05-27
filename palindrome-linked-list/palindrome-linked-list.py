# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    """
    FIRST SOLUTION USING STACK TO REVERSE FIRST HALF AND COMPARE THE REMAINING OF THE LINKED LIST
    """
    def isPalindrome(self,head):
        fast = slow = head
        stackpal = []
        while fast.next!=None and fast.next.next !=None:
            stackpal.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast.next!=None:
            stackpal.append(slow.val)
        slow = slow.next
    
        while slow is not None:
            if slow.val ==stackpal.pop():
                slow = slow.next
            else:
                return False
        return True
    
    
    
    #   # """ SECOND SOLUTION USING STACK TO REVERSE THE WHOLE LIST AND COMPARE THE ORIGINAL LINKED     LIST
    # """
    
#     def isPalindrome(self, head: ListNode) -> bool:
#         new_node = ListNode()
#         iter1 = iter2 = head 
#         prev = None
#         temp = None
      
#         while iter1 is not None:
#             temp = iter1.next
#             iter1.next = prev
#             prev = iter1
#             iter1 = temp
#         return prev
        
#         while prev !=None and iter2 != None:
#             if prev == iter2:
#                 return True
#             elif prev != iter2 and counter ==2:
#                 return False
#             iter2 = iter2.next 
#             prev = prev.next
            
        
            
    
             
            