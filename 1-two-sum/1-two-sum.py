class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #O(N) time and space cmplexity
        d = dict()
        i = 0 #store their index
        for item in nums:
            d[item] = i
            i+=1
        
        # print(d)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d[complement] != i: #ensuring its not duplicated numbers
                return [i,d[complement]]
            
   