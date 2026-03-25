class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_dict = {}
        for i in range (len(board)):
            row_dict = {}
            column_dict = {}
            for j in range(len(board[i])):
                if board[i][j]!='.' and board[i][j] in row_dict:
                    return False
                elif board[i][j]!='.':
                    row_dict[board[i][j]] = True
                if board[j][i]!='.' and board[j][i] in column_dict:
                    return False
                elif board[j][i]!='.':
                    column_dict[board[j][i]] = True
                box = (i//3) * 3 + (j//3)
                if board[i][j]!='.' and (board[i][j], box) in square_dict:
                    return False
                elif board[i][j]!='.':
                    square_dict[(board[i][j], box)] = True
      
        return True
        
                
