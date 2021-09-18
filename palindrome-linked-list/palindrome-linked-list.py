# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self,head):
        stack = []
        iter1 = iter2 = length_iter = head
        counter = 0
        while length_iter is not None:
            counter +=1
            length_iter = length_iter.next
        
        if counter%2 ==0: #even length
            step = 0
            while step < counter//2:
                stack.append(iter1.val)
                iter1 = iter1.next
                step+=1
    
            while iter1 is not None:
                if iter1.val != stack.pop():
                    return False
                iter1 = iter1.next
            return True         
            
        elif counter%2 !=0: #odd len:
            step = 1
            while step < counter//2 + 1:
                stack.append(iter1.val)
                iter1 = iter1.next
                step+=1
            iter1 = iter1.next
        
            while iter1 is not None:
                if iter1.val != stack.pop():
                    return False
                iter1 = iter1.next
            return True
            
        
            
            
    
    

    
    
    
    
    
    
    
    
    
    
    
    """
    FIRST SOLUTION USING STACK TO REVERSE FIRST HALF AND COMPARE THE REMAINING OF THE LINKED LIST
    """
#     def isPalindrome(self,head):
#         fast = slow = head
#         stackpal = []
#         while fast.next!=None and fast.next.next !=None:
#             stackpal.append(slow.val)
#             slow = slow.next
#             fast = fast.next.next
        
#         if fast.next!=None:
#             stackpal.append(slow.val)
#         slow = slow.next
    
#         while slow is not None:
#             if slow.val ==stackpal.pop():
#                 slow = slow.next
#             else:
#                 return False
#         return True
    
    
    
    #   # """ SECOND SOLUTION USING STACK TO REVERSE THE WHOLE LIST AND COMPARE THE ORIGINAL LINKED     LIST
    # """
    
#     def isPalindrome(self, head: ListNode) -> bool:
#         new_node = ListNode()
#         iter1 = iter2 = head 
#         prev = None
#         temp = None
      
#         while iter1 is not None:
#             temp = iter1.next
#             iter1.next = prev
#             prev = iter1
#             iter1 = temp
#         return prev
        
#         while prev !=None and iter2 != None:
#             if prev == iter2:
#                 return True
#             elif prev != iter2 and counter ==2:
#                 return False
#             iter2 = iter2.next 
#             prev = prev.next
            
        
            
    
             
            