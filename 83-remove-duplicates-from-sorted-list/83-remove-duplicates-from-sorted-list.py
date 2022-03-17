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
                iter1.next = iter1.next.next   #set its iter1.next to two steps ahead and check again becos of trios or more
            else: #ADDED else statement to move iter1 pointer forward when next item is different to prevent infinte loop 
                iter1 = iter1.next
        
        return head