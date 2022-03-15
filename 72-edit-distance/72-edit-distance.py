class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #time complexity O(m*n) where m and n are the length of the two strings
        #space complexity is O(m*n) where m and n are the length of the two strings since we form a 2D grid
        #https://www.youtube.com/watch?v=XYi2-LPrwm4
        
        grid = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        
        #initialize grid with extra "" rows and columns
        for i in range(len(word1)+1):
            grid[len(word2)][i] = len(word1) - i
            
        for j in range(len(word2)+1):
            grid[j][len(word1)] =  len(word2) - j
            
        #bottom-up approach
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    grid[j][i] = grid[j+1][i+1]
                else:
                    #either add (i+1,j), delete(i,j+1), or replace (i+1,j+1) with a cost of +1
                    grid[j][i]  = 1 + min(grid[j+1][i],grid[j][i+1],grid[j+1][i+1])
                    
        # print(grid)
        return grid[0][0]