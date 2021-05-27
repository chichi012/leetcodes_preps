class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                summs = nums[i]+nums[j]
                if summs == target:
                    ls = [i,j]
        return ls
        
        # time complexity = O(n^2)
        #space = O(1)