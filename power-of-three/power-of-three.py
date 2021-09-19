class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ls = [3**i for i in range(0,31)]
        if n >0 and n in ls:
            return True
        