# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        iter1 = head
        
        while iter1 is not None and iter1.next is not None: 
            if iter1.val == iter1.next.val:
                iter1.next = iter1.next.next
            else:
                iter1 = iter1.next
        return head