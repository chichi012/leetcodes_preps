class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #Negative marking solution
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            else:
                nums[cur] = -nums[cur]
                
                
        return duplicate
        
        
