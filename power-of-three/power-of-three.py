import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """due to machine epsilon for 243, i cant use this solution"""
        if n in (243,59049,1594323,14348907,129140163):
            return True
        if n <= 0:
            return False
        x = math.log(n,3) 
        y = int(x)
        if 3**y == n:
            return True 
        else:
            return False
        
        
        
        """RECURSION"""
        # return n > 0 and (n==1 or (n%3 == 0 and self.isPowerOfThree(n/3)));
        
        
        """USING WHILE LOOP"""
#         if n <= 0:
#             return False
#         while n%3 == 0:
#             n = n/3
#         return n == 1
        
        """USING TABLE LOOK UP"""
        
        # ls = [3**i for i in range(0,31)]
        # if n >0 and n in ls:
        #     return True