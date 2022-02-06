class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#      Approach: https://www.youtube.com/watch?v=uDB5QXTqMn0
#      1. Loop through grid[row][col] for "1"s. Call a depth first search on it 
#      2. Mark grid[row][col] as seen then check its neighbours, Call a depth first search on "1"s encountered
#      3. After dfs call, increment num_islands count and return 
        """
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","1","1","0"]
        """
        num_islands  = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "1":
                    print(row_index)
                    self.numIslandsHelper(grid,row_index,col_index)
                    num_islands +=1
        return num_islands

    def numIslandsHelper(self,grid,r,c):
        #mark as seen
        grid[r][c] = "0"
        #next check neighbours [up,down,left,right]
        neighbours = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for row,col in neighbours:
            if row >=0 and col >=0 and row < len(grid) and col<len(grid[row]) and grid[row][col] == "1":
                self.numIslandsHelper(grid,row,col)
                
        