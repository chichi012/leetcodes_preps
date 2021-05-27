# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        iter1 = head
        counter = 0
        while iter1 is not None:
            counter+=1
            iter1 = iter1.next
        iter1 = iter2 = head
        if counter % 2 !=0:
            while iter2.next is not None:
                iter1 = iter1.next
                iter2 = iter2.next.next
            return iter1
        elif counter % 2 ==0:
            for i in range(counter//2):
                iter1 = iter1.next
            return iter1
                

        