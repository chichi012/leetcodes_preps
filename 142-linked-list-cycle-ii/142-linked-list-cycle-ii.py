# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = dict()
        iter1 = head
        ind = -1
        
        while iter1:
            if iter1 in d:
                # print(d[iter1])
                return iter1
                
            ind+=1
            d[iter1] = ind
            iter1 = iter1.next
            
        return