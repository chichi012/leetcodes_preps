# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        iter1 = head
        length = 0
        while iter1 is not None:
            length +=1
            iter1 = iter1.next
        indices = length -1 
        iter1 = head
        summa = 0
        while iter1 is not None:
            summa += iter1.val * (2**(indices))
            iter1 = iter1.next
            indices -=1
        return summa
        

        