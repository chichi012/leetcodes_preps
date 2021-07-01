# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        iter1 = head
        set_ = set()
        while iter1 is not None and iter1 not in set_:
            set_.add(iter1)
            iter1 = iter1.next
        if iter1 is None:
            return None
        else:
            return iter1
        
        