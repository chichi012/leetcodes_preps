class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map= {}
        for i,num in enumerate(nums):
            hash_map[num] = i
            
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hash_map and hash_map[complement] != j:
                return [j,hash_map[complement]]
        
       

        
        
        
        
        
        
        # not working yet
#         arr =  sorted(nums)
#         l_pointer = 0
#         r_pointer = len(nums)-1
#         while l_pointer < r_pointer:
#             if arr[l_pointer] + arr[r_pointer] == target:
#                 return [nums.index(arr[l_pointer]),nums.index(arr[r_pointer])]
#             if arr[l_pointer] + arr[r_pointer] < target:
#                 l_pointer = l_pointer + 1
#             elif arr[l_pointer] + arr[r_pointer] > target:
#                 r_pointer = r_pointer - 1     
        
        

    
        
        
        
#         ls = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 summs = nums[i]+nums[j]
#                 if summs == target:
#                     ls = [i,j]
#         return ls
        
        # time complexity = O(n^2)
        #space = O(1)