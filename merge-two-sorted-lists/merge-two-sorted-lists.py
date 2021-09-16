# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        iter1 = l1
        iter2 = l2
        iter3 = l3 = ListNode()
        
        while iter1 is not None and iter2 is not None:
            if iter1.val <= iter2.val:
                iter3.next = iter1
                iter1 = iter1.next
            elif iter1.val > iter2.val:
                iter3.next = iter2
                iter2 = iter2.next
            iter3 = iter3.next
            
        if iter1 is not None:
            iter3.next = iter1
        elif iter2 is not None:
            iter3.next = iter2
        
        return l3.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#         iter1 = l1
#         iter2 = l2
#         iter3 = l_list = ListNode() 
        
#         while iter1 is not None and iter2 is not None:
#             if iter1.val <= iter2.val:
#                 iter3.next = iter1
#                 iter1 = iter1.next         
                
#             elif iter1.val > iter2.val:
#                 iter3.next = iter2 
#                 iter2 = iter2.next
#             iter3 = iter3.next
                
#         if iter1 is not None:
#             iter3.next = iter1
#         elif iter2 is not None:
#             iter3.next = iter2
            
#         return l_list.next
            
        
        
        
        
      
        
#         iter1 = l1
#         iter2 = l2 
#         l_list = ListNode()
#         # l_list = iter_list = ListNode()
#         iter_list = l_list
#         while iter1 is not None and iter2 is not None:
#             if iter1.val <= iter2.val:
#                 iter_list.next = iter1
#                 iter1 = iter1.next
                
#             else: #iter1.val > iter2.val:
#                 iter_list.next = iter2
#                 iter2 = iter2.next
#             iter_list = iter_list.next
                
#         # return iter_list
        
#         if iter1 is not None:
#             iter_list.next = iter1
#         elif iter2 is not None:
#             iter_list.next = iter2
#         return l_list.next
    
                
                