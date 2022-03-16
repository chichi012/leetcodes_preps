class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force - O(n) time, O(n) space
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1,j+1]
#                 elif numbers[i] + numbers[j] > target:
#                     continue

# or using the dictionary mehtod is brute force as well since its O(n) time, O(n) space
# https://leetcode.com/problems/two-sum/

                    
    
        #TWO POINTER METHOD  O(n) time, O(1) space
        left = 0
        right =  len(numbers)-1
        
        while left<right:
            sums = numbers[left]+numbers[right]
            if sums < target:
                left +=1
            if sums >target:
                right -=1
            elif sums == target:
                return [left+1,right+1] #since array is 1-indexed and ours is 0-indexed
            
        return []
        

        
        