# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = head
        prev = None
        temp = None
        
        while iter1:
            temp = iter1.next
            iter1.next = prev
            prev = iter1
            iter1 = temp
            
        return prev
        