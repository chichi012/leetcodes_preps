# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        iter1 = head
        
        while iter1 and iter1.next:
            if iter1.val == iter1.next.val:
                iter1.next = iter1.next.next
            else: #ADDED else statement to prevent cases of trios or more
                iter1 = iter1.next
        
        return head