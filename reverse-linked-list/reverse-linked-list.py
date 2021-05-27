# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        
        iter1 = head
        prev = None
        temp = None
        
        while iter1 is not None:
            temp =iter1.next
            iter1.next = prev
            prev = iter1
            iter1 = temp
        return prev
        
        
        
        
        
        
        
        
        
        
        
#         l_list = ListNode()
#         iter_list = l_list
#         iter1 = head
#         while iter1 is not None:
#             iter_list = iter1
#             iter1 = iter1.next
            
#         return l_list
       
    