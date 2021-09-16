# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
     
        # iter1 = head
#         prev = None
#         temp = None
        
#         while iter1 is not None:
#             temp =iter1.next
#             iter1.next = prev
#             prev = iter1
#             iter1 = temp
#         return prev

        return self.reverseListHelper(head)
        
        
    def reverseListHelper(self,iter1,prev=None):
        if not iter1:
            return prev
        temp = iter1.next
        iter1.next = prev
        prev = iter1
        return self.reverseListHelper(temp,iter1)

        
        
        
        
        
        
        

    