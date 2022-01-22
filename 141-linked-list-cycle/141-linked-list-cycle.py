# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        iter1 = head
        while iter1:
            if iter1 in s:
                return True
            else:
                s.add(iter1)
                iter1 = iter1.next
            