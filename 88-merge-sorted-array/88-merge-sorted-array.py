class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.      
        """
        pointer = m+n-1
        arr = [None]*len(nums1)
        
        while m >0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[pointer] = nums1[m-1]
                m-=1
            else:
                nums1[pointer] = nums2[n-1]
                n-=1
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


        
#         p1 = p2 = 0
#         if m == 0 and n!=0:
#             nums1[p1] = nums2[p2] 
        
#         if n and m:
#             for _ in range(m):
#                 if nums1[p1] <= nums2[p2]:
#                 # and nums1[p1] !=0: 
#                     p1+=1
#                 else:
#                     nums1[p1],nums2[p2] = nums2[p2],nums1[p1]
#                     p2+=1

#             for _ in range(p1,len(nums1)) :
#                 nums1[p1] = nums2[p2]
#                 p1+=1
#                 p2+=1



