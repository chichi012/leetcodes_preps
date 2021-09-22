# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """STRATEGY
        1. get to middle of linkedlist and separate them
        2. reverse second half
        3. re-arrange pointers
        """ 
        
        
#         step 1
        
        fast = slow = head
        while fast.next is not None and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_l = slow.next
        slow.next = None
        
        
#      step 2
        iter1 = new_l
        prev = None
        temp = None
        while iter1 is not None:
            temp = iter1.next
            iter1.next = prev
            prev = iter1
            iter1 = temp
        # print("head left =====",head)
        # print("reversed =====",prev)
        #note that reversed list is prev
        
         
#             step 3

      
        first_half = head
        second_half = prev
        temp = None
     
        while second_half is not None:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp
            
            temp  = second_half.next
            second_half.next = first_half
            second_half = temp
            
            
        # print("final ans =======", head)

            
        
        
        
        
        
        
        
        
        
#         sett = set()
#         iter1 = head
#         tail = None
#         while iter1:
#             sett.add(iter1)
#             iter1 = iter1.next
        
#         dummy = ListNode()
#         dummy.next = head
#         iter2 = dummy
        
#         while iter2.next in sett:
#             iter2.next = 
            
#     def tail(self,val):
#         new_node = ListNode(val)
#         if self.head is None:
#             self.head = self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node