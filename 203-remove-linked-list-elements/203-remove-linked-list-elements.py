# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev =dummy = ListNode(0,head)
        iter1 = head
        while iter1:
            prev.next = iter1
            if iter1.val == val:
                prev.next = iter1.next
                iter1 = iter1.next
            else:
                prev = iter1
                iter1 = iter1.next
                
        return dummy.next
            