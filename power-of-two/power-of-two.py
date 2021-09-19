import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n,2)
        y = int(x)
        if 2**y == n:
            return True
        else:
            return False
     
        