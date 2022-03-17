class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        USING TWO POINTERS
        time complexity: O(N) since we need to traverse the nums list once to check all its elements
        Space complexity: O(1)
        
        Strategy: [0,0,1,2,2,3,3,4,5,6,6]
        
        - first element will always come first so start two pointers at second element index arr[1]
        - left, right = 1, 1 
        
         [0,0,1,2,2,3,3,4,5,6,6]
            r
            l
           
        - left will point to the position that needs to be filled based on right's comparison with its previous neighbor
        
        [0,0,1,2,2,3,3,4,5,6,6] : arr[r] != arr[r-1] (meaning its a new number) so we fill in arr[l] = arr[r], then increament both pointers
           r -
           l
        
        [0,1,1,2,2,3,3,4,5,6,6] arr[r] != arr[r-1] so we fill in arr[l] = arr[r], then increament both pointers
             l
             r
            
        [0,1,2,2,2,3,3,4,5,6,6] since arr[r] == arr[r-1] so we keep moving forward with r and dont update left
               l
               r r
               
        at the end, return the left pointer(exactly its number) since that wil give the "k" distinct elements
        
        """
        left = 1
        
        for right in range(1,len(nums)):
            #enter condition only if tree, else increment right pointer
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
            #the for loop takes care of the increment of right pointer
                
        return left
                
            
            
            
            
            
            
            
            
            
            
            
            
            