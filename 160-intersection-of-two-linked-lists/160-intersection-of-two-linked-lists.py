# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #this is O(N+M) time and O(1) space
        #Loop through each Llist, get their lengths. move longer llist by their difference
        #then return node where they meet 
        
        iter1 = headA
        iter2 = headB
        a,b = 0,0
        
        while iter1:
            a+=1
            iter1 = iter1.next
            
        while iter2:
            b+=1
            iter2 = iter2.next
            
        if a>b:
            diff = a-b
            #start at beginning again
            long = headA
            short = headB
        else:
            diff = b-a
            long = headB
            short = headA
            
        for i in range(diff): #move longer llist by difference
            long = long.next
        
        while long != short:
            long = long.next
            short = short.next
        
        return short
            
    
            
        
        
        
        
        
        
#         Solution 2
        
        #this is O(N+M) time and space
#         s = set()
#         iter1 = headA
#         iter2 = headB
        
#         while iter1 is not None:
#             s.add(iter1)
#             iter1 = iter1.next
            
#         while iter2 is not None:
#             if iter2 in s:
#                 return iter2
#             s.add(iter2)
#             iter2 = iter2.next
            
#         return
        
        