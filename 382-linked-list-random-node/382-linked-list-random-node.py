# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
    #Solution 2: RESERVOIR SAMPLING
    #Space complexity is O(1)
    #Time complexity is O(1)
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    #Time complexity is O(N) where NN is the number of elements in the input list.
    def getRandom(self) -> int:
        scope = 1 
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value


#  Solution 1: convert the linked list into an array. Uses extra space and cant cater to large list
#O(N) space and time complexity

#     def __init__(self, head: Optional[ListNode]):
#         self.head = head
        
#     def getRandom(self) -> int:
#         l =[]
#         iter1 = self.head
#         while iter1:
#             l.append(iter1.val)
#             iter1 = iter1.next

#         return random.choice(l)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()