# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """this worked"""
#         iter1 = list1
#         iter2 = list2
#         iter3 = l_list = ListNode()
        
#         self.mergeTwoListsHelper(iter1,iter2,iter3)
        
#         return l_list.next;
    
#     def mergeTwoListsHelper(self,iter1,iter2,iter3):
#         if iter1 is None and iter2 is None:
#             return 
#         elif iter1 is not None and iter2 is None:
#             iter3.next = iter1
#             return
#         elif iter2 is not None and iter1 is None:
#             iter3.next = iter2 
#             return
#         if iter1.val <= iter2.val:
#             iter3.next = iter1
#             self.mergeTwoListsHelper(iter1.next, iter2, iter3.next)
#         elif iter1.val > iter2.val:
#             iter3.next = iter2 
#             self.mergeTwoListsHelper(iter1, iter2.next, iter3.next)
            
        iter1 = list1
        iter2 = list2
        node = dummy_node = ListNode()
        if iter1 is None and iter2 is None:
            return
        while iter1 is not None and iter2 is not None:
            if iter1.val <= iter2.val:
                node.next = iter1
                iter1 = iter1.next
            elif iter1.val > iter2.val:
                node.next = iter2
                iter2 = iter2.next
            node = node.next
            
        if iter1 is not None and iter2 is None:
            node.next = iter1
            
                
        if iter2 is not None and iter1 is None:
            node.next = iter2
            
        return dummy_node.next
            
        