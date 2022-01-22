# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Tortoise and Hare algorithm (two pointers method)
        ## Using hash set. O(N)time and O(1) space complexity
        fast =  head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            
        return False
        
        
        
        # Using hash set. O(N) Space-time complexity
#         s = set()
#         iter1 = head
#         while iter1:
#             if iter1 in s:
#                 return True
#             else:
#                 s.add(iter1)
#                 iter1 = iter1.next
            