class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appears = False
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                appears = True
                return appears
        return appears
            
            
        