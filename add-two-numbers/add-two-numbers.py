# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ITERATIVE"""
        iter1 = l1
        iter2 = l2
        iter3 = ans = ListNode()
        carry = 0
        sums = 0
        
        while iter1 is not None and iter2 is not None:
            sums = (iter1.val + iter2.val + carry)
            carry = sums//10
            unit = sums%10
            iter3.next = ListNode(unit)
            iter1 = iter1.next
            iter2 = iter2.next
            iter3 = iter3.next
            
   
        while iter1 is not None:
            sums = iter1.val + carry
            carry = sums//10
            unit = sums%10
            iter3.next = ListNode(unit)
            iter1 = iter1.next
            iter3 = iter3.next

        while iter2 is not None:
            sums = iter2.val + carry
            carry = sums//10
            unit = sums%10
            iter3.next = ListNode(unit)
            iter2 = iter2.next
            iter3 = iter3.next
        
        if iter1 is None and iter2 is None and carry!=0:
            iter3.next = ListNode(carry)
        
        return ans.next
            
            
             
            
            
        