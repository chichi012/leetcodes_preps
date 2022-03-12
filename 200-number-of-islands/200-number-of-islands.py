class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#      Approach: https://www.youtube.com/watch?v=uDB5QXTqMn0
#      1. Loop through grid[row][col] for "1"s. Call a depth first search on it 
#      2. Mark grid[row][col] as seen then check its neighbours, Call a depth first search on "1"s encountered
#      3. After dfs call, increment num_islands count and return 
        """
      0,0,0,0,0,0,0,0,0,0,0,0  
      0["1","1","1","1","0"],0
      0["1","1","0","1","0"],0
      0["1","1","0","0","0"],0
      0["0","0","1","1","0"],0
      0,0,0,0,0,0,0,0,0,0,0,0
        """
        
        #input - grid
        #output - integer count of num of islands
        #BFS OR DFS

        #using a DFS
        
        counter  = 0
        #traverse the rows and columns
        
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "1":
                    self.numIslandsHelper(grid,row_index,col_index)
                    counter += 1
                    
        return counter
    
    def numIslandsHelper(self,grid,r,c):
        #mark grid[r][c] as seen to avoid it being counted twice when traversing neighbours 
        grid[r][c] = "0" #mark seen
        
        #next we check for adjacent lands horizontally or vertically coordinates (row,col)
        up = (r - 1 , c)
        down = (r + 1,c)
        left = (r, c - 1)
        right = (r, c + 1)
        
        neighbours = [up,down,left,right]
        
        for row,col in neighbours:
            #set the boundaries
            if row >=0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == "1":
                #then call helper function again
                self.numIslandsHelper(grid,row,col)
                


    
    
    
#         num_islands  = 0
#         for row_index in range(len(grid)):
#             for col_index in range(len(grid[row_index])):
#                 if grid[row_index][col_index] == "1":
#                     print(row_index)
#                     self.numIslandsHelper(grid,row_index,col_index)
#                     num_islands +=1
#         return num_islands

#     def numIslandsHelper(self,grid,r,c):
#         #mark as seen
#         grid[r][c] = "0"
#         #next check neighbours [up,down,left,right]
#         neighbours = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
#         for row,col in neighbours:
#             if row >=0 and col >=0 and row < len(grid) and col<len(grid[row]) and grid[row][col] == "1":
#                 self.numIslandsHelper(grid,row,col)
                
        