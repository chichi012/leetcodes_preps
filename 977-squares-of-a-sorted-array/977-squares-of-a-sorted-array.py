class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums)-1
        pointer = right_pointer
        arr = [None]*len(nums)
        
        while left_pointer<= right_pointer:
            left_square = nums[left_pointer] * nums[left_pointer]
            right_square =nums[right_pointer] * nums[right_pointer]
            
            if left_square > right_square:
                arr[pointer] = left_square
                left_pointer +=1
                
            else:
                arr[pointer] = right_square
                right_pointer -=1
            pointer -=1
            
        return arr
                
        
        
        
        
        
        # for x in range(len(nums)):
        #     nums[x] = nums[x]*nums[x]
        # e = sorted(nums)
        # return e
        
        