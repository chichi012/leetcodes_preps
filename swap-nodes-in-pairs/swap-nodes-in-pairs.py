# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dummy = ListNode()
        dummy.next = head
        res = head if not head.next else head.next
        while dummy.next and dummy.next.next:
            temp = dummy.next
            dummy.next = temp.next
            temp.next = temp.next.next
            dummy.next.next = temp
            dummy = temp
            
        return res
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     iter1 = pre.next
        #     iter2 = a.next
        #     pre.next, iter2.next, iter1.next = iter2, iter1, iter2.next
        #     pre = iter1
        # return self.next
        
        