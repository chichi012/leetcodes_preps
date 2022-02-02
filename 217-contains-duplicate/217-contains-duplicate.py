class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #O(N) space and time complexity.
        dicct  = dict()
        for item in nums:
            if item not in dicct:
                dicct[item] = 1
            else:
                dicct[item] +=1
        for _,value in dicct.items():
            if value >=2:
                return True
                

        
#         Solution 2
#         O(N logN) Time complexity and O(1) space
        # num = sorted(nums)
        # for i in range(len(num)-1):
        #     if num[i] == num[i+1]:
        #         return True
        # return False