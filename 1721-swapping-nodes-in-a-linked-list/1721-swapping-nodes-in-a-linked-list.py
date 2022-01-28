# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #get te pointers in place then replace
        # -- Method 1: Back tracking with recursion
        # -- Method 2: get length of llist to find kth node
        
        #get to the kth index. remember its 1-indexed
        iter1 = head
        for _ in range(k-1):
            iter1 = iter1.next
            
        #now iter1 is at kth index. put the fast pointer here
        fast = iter1
        slow = head
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #slow pointer is pointing at kth node from end and 
        #iter1 is at kth node from start
        
        #doing the swapping of node values
        iter1.val,slow.val = slow.val,iter1.val
        
        return head
        
        
        