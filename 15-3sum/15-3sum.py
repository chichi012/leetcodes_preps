class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #total time complexity: O(NlogN) + O(N^2) = O(N^2)   (keep dominant term)
        #space complexity: depends on sorting implementation. Could be O(1) or O(N)
        
        if not nums or (len(nums) == 1 and nums[0] == 0):
            return []
        arr = []
        nums.sort()   #O(NlogN) Time complexity
        
        #use each number in the input array as a possible first value
        for i,a in enumerate(nums):  
            #check that next number isnt the same as previous and i isnt the first number in the array. If a==nums[i-1],  skip this loop
            if i > 0 and a==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:                         #O(N*N) Time complexity
                sums = a+ nums[left]+nums[right]
                if sums > 0:
                    right -=1        
                elif sums < 0:
                    left +=1
                else:
                    ls = [a,nums[left],nums[right]]
                    arr.append(ls)
                    #move the left pointer or right pointer only since the other conditions will take care of the other pointer
                    left +=1
                    #skip next number if the same again
                    while left < right and nums[left] == nums[left-1]:
                        left +=1

                    
        return arr
                    
                    
                
# [-1,0,1,0]
        