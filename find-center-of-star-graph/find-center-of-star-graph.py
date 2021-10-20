class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """ easy approach:
        check the first two edges, the number that appears in both is the answer
        """
        ls1 = set(edges[0])
        ls2 = set(edges[1])
        return list(ls1.intersection(ls2))[0]