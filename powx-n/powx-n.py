class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = -n 
            x = 1/x
            return pow(x,n)
        else:
            return pow((x*x),n/2) if n%2==0 else x*pow((x*x),n//2)

        
        
        
        
        
        
        
        """BRUTE FORCE"""
        # return x**n