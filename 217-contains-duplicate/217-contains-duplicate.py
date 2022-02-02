class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicct  = dict()
        for item in nums:
            if item not in dicct:
                dicct[item] = 1
            else:
                dicct[item] +=1
        for _,value in dicct.items():
            if value >=2:
                return True
                