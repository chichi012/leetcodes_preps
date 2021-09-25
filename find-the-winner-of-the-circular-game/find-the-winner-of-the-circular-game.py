class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
#         ls = [i for i in range(1,n+1)]
#         print(ls)
#         return self.findTheWinnerHelper(ls,k)
        
#     def findTheWinnerHelper(self,ls,k):
#         if not ls:
#             return
#         if len(ls) ==1:
#             return ls[0]
#         else:
#             while loop
    
        