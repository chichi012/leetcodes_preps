class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_path = set()
    
        def existHelper(r,c,i):
            #mark as seen
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[row]) or word[i] != board[r][c] or (r,c) in word_path:
                return False
            
            
            word_path.add((r,c))
            result = (existHelper(r-1,c,i+1) or 
                      existHelper(r+1,c,i+1) or
                      existHelper(r,c+1,i+1) or
                      existHelper(r,c-1,i+1)           
                     )
            
            word_path.remove((r,c))
            # directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            return result
            
#             for row,col in directions:
#                 if row >= 0 and col > = 0 and row < len(board) and col < len(board[row]) and board[row][col] in word_split:
#                     existHelper(board,row,col)
                    
                    
        for row in range(len(board)):
            for col in range(len(board[row])):
                if existHelper(row,col,0):
                    return True
        return False