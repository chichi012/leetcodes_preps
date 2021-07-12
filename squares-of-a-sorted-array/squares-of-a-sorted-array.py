import sys
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

 #using two pointers method with O(n) TIME AND SPACE 
        left_pointer = 0
        right_pointer = len(nums)-1
        answer_array = [0] * len(nums)
        insert_pointer = right_pointer
        while left_pointer <= right_pointer:
            left_square = nums[left_pointer] * nums[left_pointer]
            right_square = nums[right_pointer] * nums[right_pointer]
            
            if left_square <= right_square:
                answer_array[insert_pointer] = right_square
                right_pointer -=1
                
            else:
                answer_array[insert_pointer] = left_square
                left_pointer +=1
            insert_pointer -=1
        return answer_array
                
            
#             if nums[left_pointer]> nums[right_pointer]:
#                 sorted_ls[-1] = nums[left_pointer]
                
#                 left_pointer = left_pointer +1
#             elif (nums[left_pointer]*nums[left_pointer]) < nums[right_pointer]*nums[right_pointer]:
#                 sorted_ls.append(nums[right_pointer]*nums[right_pointer])
#                 right_pointer = right_pointer -1
#         return sorted_ls
        
        
        
        
#         time limit exceeded
#     n = len(nums)
#         for i in range(len(nums)):
#             nums[i] = abs(nums[i] * nums[i])
        
#         for i in range(len(nums)):
#             swapped =False
#             for j in range(0,n-1-i):
#                 if nums[j]> nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1],nums[j]
#                     swapped = True

#         return nums
        
        
        
        
        
        
        
        
#         this is the brute force solution

#         for i in range(len(nums)):
#             nums[i] = abs(nums[i] * nums[i])
#         ls = sorted(nums)
#         return ls
        
