import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """SOLUTION WITH LOOPS"""
        if n <= 0:
            return False
        while n%2 == 0:
            n= n/2
        return n==1
        
        
        
        
        
        
        
        """BRUTE FORCE WITHOUT LOOP / RECURSION"""
        # if n <= 0:
        #     return False
        # x = math.log(n,2)
        # y = int(x)
        # if 2**y == n:
        #     return True
        # else:
        #     return False
     
        