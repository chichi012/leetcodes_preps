class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.      
        
         O(N) time and O(1) Space
         
        This question manages 3 pointers
        nums1 = [1,2,3,0,0,0]
                   [m-1]   p
        
        nums2 = [2,5,6]
                    [n-1] pointer and 
        
        compare 6 > 3: so fix 6 at nums1[p]
        then decrease ""[n-1] pointer" and "p"
        
        
"""
        #get last pointer in nums1 and fill them in reverse order
        pointer = m+n-1
        
        
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                #if pointer in m > n then put figure at nums1[m] at nums[pointer] position
                nums1[pointer] = nums1[m-1]
                m-=1
                #then decrease m pointer
            else: #if pointer in m < n then put figure at nums1[n] at nums[pointer] position
                nums1[pointer] = nums2[n-1]
                n-=1  
                #then decrease n pointer
            
            #pointer decreases in both cases
            pointer -=1
            
        #attach the remainder of nums2 into nums1 if any
        if n:
            nums1[:n] = nums2[:n]

        

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         while m > 0 and n > 0:
#             if nums1[m - 1] > nums2[n - 1]:
#                 nums1[m + n - 1] = nums1[m - 1]
#                 m -= 1
#             else:
#                 nums1[m + n - 1] = nums2[n - 1]
#                 n -= 1
#         nums1[:n] = nums2[:n]




