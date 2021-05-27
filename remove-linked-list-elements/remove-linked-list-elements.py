# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #create a dummy head with val -1 not part of linked list
        dummy_head = ListNode(-1)
        dummy_head.next = head
        iter1 = dummy_head
        if iter1 is None:
            return None
 
        while iter1.next is not None:
            if iter1.next.val == val:
                iter1.next = iter1.next.next
            else:
                iter1 = iter1.next
        return dummy_head.next
                
                
        
        
        