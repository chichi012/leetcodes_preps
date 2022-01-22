# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        iter1 = head
        dummy = prev = ListNode(0,head)
        while iter1 and iter1.next:
            #get pointers for next pair to swap
            nextPair= iter1.next.next
            iter2 = iter1.next
            
            #swapping
            iter2.next = iter1
            iter1.next = nextPair
            prev.next = iter2
            
            #update pointers
            prev = iter1
            iter1 = iter1.next
            
            
        return dummy.next
        