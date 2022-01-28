# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #Approach 2: using bit manipulation
        #Time complexity:O(N) , Space: O(1)
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val #10 + 0 = 10 converted to 2
            head = head.next
        return num
        
        
#         O(N) time and O(1) space

        #approach 1: get length of binary number, and convert the usual way
#         length = 0
#         iter1 = head
#         while iter1:
#             length +=1
#             iter1 = iter1.next
        
#         #since it starts at 0 index when expanding, subtract 1
#         indices = length - 1 
        
#         iter1 = head
#         summ = 0
#         while iter1:
#             summ += iter1.val * (2**(indices))
#             iter1 = iter1.next
#             indices -=1
            
#         return summ
        
        