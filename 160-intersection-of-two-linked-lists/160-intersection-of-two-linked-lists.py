# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        iter1 = headA
        iter2 = headB
        
        while iter1 is not None:
            s.add(iter1)
            iter1 = iter1.next
            
        while iter2 is not None:
            if iter2 in s:
                return iter2
            s.add(iter2)
            iter2 = iter2.next
            
        return
        
        