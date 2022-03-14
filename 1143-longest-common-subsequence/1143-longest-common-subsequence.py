class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #tabulation Dynamic Programming with Bottom-Up approach
        # time complexity: O(nxm) where n and m are the length of the two strings
        #space complexity: 2D matrix of length nxm
        grid = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
        print(grid)
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if text2[i] == text1[j]:
                    print(text2[i],text1[j])
                    grid[i][j] = 1 + grid[i+1][j+1]  # 1 + diagonal
                    
                else:
                    grid[i][j] = max(grid[i+1][j],grid[i][j+1])
                    
        return grid[0][0]
        