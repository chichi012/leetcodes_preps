class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        """SET THEORY"""
        a = set(nums1).intersection(nums2)
        b = set(nums3).intersection(nums2)
        c = set(nums3).intersection(nums1)
        return a.union(b).union(c)
        

        """BRUTE FORCE WAY"""
        ls = []
        for i in nums1:
            if i in nums2 or i in nums3:
                ls.append(i)
                
        for i in nums2:
            if i in nums1 or i in nums3:
                ls.append(i)
                
        for i in nums3:
            if i in nums1 or i in nums2:
                ls.append(i)     
        
        return list(set(ls))
                
