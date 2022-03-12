class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #create a hashmap fr the arrays
        
        dict_a, dict_b, dict_c, dict_d = {},{},{},{}

        for num in nums1:
            if num not in dict_a:
                dict_a[num] = 0
            dict_a[num] += 1
                
        for num in nums2:
            if num not in dict_b:
                dict_b[num] = 0
            dict_b[num] += 1
                
        for num in nums3:
            if num not in dict_c:
                dict_c[num] = 0
            dict_c[num] += 1
                
        for num in nums4:
            if num not in dict_d:
                dict_d[num] = 0
            dict_d[num] += 1
                  
        print('dict_a',dict_a )
        print('dict_b',dict_b )
        print('dict_c',dict_c )
        print('dict_d',dict_d )


        #keep track of their sums and  combination of times they appear to use in the final combo
        dict_1, dict_2 = {}, {}
        
        for k in dict_a:
            for k2 in dict_b:
                if k + k2 not in dict_1:
                    dict_1[ k + k2] = dict_a[k] * dict_b[k2]
                    #thats the combination of times they appear 
                else:
                    dict_1[ k + k2] = dict_1[ k + k2] + dict_a[k] * dict_b[k2]
                    
                    
        for k in dict_c:
            for k2 in dict_d:
                if k + k2 not in dict_2:
                    dict_2[ k + k2] = dict_c[k] * dict_d[k2]
                    #thats the combination of times they appear 
                else:
                    dict_2[ k + k2] = dict_2[ k + k2] + dict_c[k] * dict_d[k2]
                    
        print('dict1',dict_1)
        print('dict2',dict_2)

        #now, to get the final combination
        counter = 0
        
        for key in dict_1:
            complement = 0 - key
            if complement in dict_2:
                counter += dict_1[key] * dict_2[complement]
                
        return counter
            
        
# [0,1,3]
# [0,-2,1]
# [0,-1,-2]
# [0,0,0]

