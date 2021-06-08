class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # https://www.youtube.com/watch?v=pV2kpPD66nE solution 2
        # solution 1
        if not grid:
            return 0
        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] =='1':
                    self.dfs(grid,r,c)
                    num_islands+=1
        return num_islands
        
        
    def dfs(self,grid,r,c):
        grid[r][c] = '0'  #marking it as seen so it doesnt get counted again
        neighbours = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for row,col in neighbours:
            if row >=0 and col>=0 and row<len(grid) and col <len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid,row,col)
                
        
      