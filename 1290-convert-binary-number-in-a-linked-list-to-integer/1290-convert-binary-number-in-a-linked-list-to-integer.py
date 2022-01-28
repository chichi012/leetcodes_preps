# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #approach 1: get length of binary number, and convert the usual way
        length = 0
        iter1 = head
        while iter1:
            length +=1
            iter1 = iter1.next
        
        #since it starts at 0 index when expanding, subtract 1
        indices = length - 1 
        
        iter1 = head
        summ = 0
        while iter1:
            summ += iter1.val * (2**(indices))
            iter1 = iter1.next
            indices -=1
            
        return summ
        
        