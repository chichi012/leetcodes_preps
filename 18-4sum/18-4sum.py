class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #first sort the array
        nums.sort()
        result, ls = [],[]
        
        # k is the number of sums. In this cse, k = 4(4Sums)
        # no need to pass in nums list since the function is embedded
        def kSum(k, start, target):
            if k != 2:
                #ensure atleast ithas remaining numbers [a,_,_,_]
                for i in range(start, len(nums) - k + 1):
                    #check that number after isnt same as number before it
                    if i >start and nums[i] == nums[i-1]:
                        continue
                    ls.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    ls.pop()
                return
            
            #base case if k = 2, perform a TwoSum
            left = start
            right = len(nums)-1
            
            while left < right:
                if nums[left] + nums[right] < target:
                    #increment left pointer
                    left+=1
                elif nums[left] + nums[right] > target:
                    #decrement right pointer
                    right -=1
                    
                else:
                    result.append(ls + [nums[left],nums[right]])
                    # print(result)
                    #increment any of the pointers.choosing left
                    left +=1
                    
                    while left <right and nums[left] == nums[left -1]:
                        left +=1
            return result
                        
        kSum(4,0,target)
        return result
