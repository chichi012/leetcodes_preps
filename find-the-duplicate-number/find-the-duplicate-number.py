class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        r = 0
        l =len(nums) -1
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return nums[j]
        
        
        
        # while r != l:
        #     if nums[r] == nums[l]:
        #         return nums[r]
        #     prev_r = r
        #     r = r+1
        #     prev
        
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])
        