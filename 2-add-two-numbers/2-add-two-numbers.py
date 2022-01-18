# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
#         d_sum = l1.val + l2.val
#         carry = d_sum//10
#         remainder = d_sum%10
#         result = ListNode(remainder)
        
#         if l1.next or l2.next or carry:
#             l1 = l1.next if l1.next else ListNode(0)
#             l2 = l2.next if l2.next else ListNode(0)
#             l1.val = l1.val + carry
#             result.next = self.addTwoNumbers(l1,l2)
            
#         return result
        
        
        
        iter1 = l1
        iter2 = l2
        carry = 0
        iter3 = l_list = ListNode()
        d_sum = 0
        
        while iter1 is not None and iter2 is not None:
            d_sum = iter1.val + iter2.val + carry
            carry = d_sum//10
            remainder = d_sum%10
            iter3.next = ListNode(remainder)
            iter1 = iter1.next
            iter2 = iter2.next
            iter3 = iter3.next
            
        while iter1 is not None:
            d_sum = iter1.val + carry
            carry = d_sum//10
            remainder = d_sum%10
            iter3.next = ListNode(remainder)
            iter1 = iter1.next
            iter3 = iter3.next
        while iter2 is not None:
            d_sum = iter2.val + carry
            carry = d_sum//10
            remainder = d_sum%10
            iter3.next = ListNode(remainder)
            iter2 = iter2.next
            iter3 = iter3.next
            
        if carry !=0 and iter1 is None and iter2 is None:
            iter3.next = ListNode(carry)
        return l_list.next
            
            
        