class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1,j+1]
#                 elif numbers[i] + numbers[j] > target:
#                     continue
                    
    
        #TWO POINTER METHOD
        left = 0
        right =  len(numbers)-1
        
        while left<right:
            sums = numbers[left]+numbers[right]
            if sums < target:
                left +=1
            if sums >target:
                right -=1
            elif sums == target:
                return [left+1,right+1]
            
        return []
        

        
        