class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ls = [4**i for i in range(0,30)]
        if n in ls:
            return True
        