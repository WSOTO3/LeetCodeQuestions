class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 # A defaultdict is a dictionary that doesnt raise the KeyError cause it provides a default value for a key
 # When initialized with set, each new key automatically gets an emptyset as its value
        
        #creating defaultdict(set) for columns,rows, and square sections 
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        # going through each box in the sudoku board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if the box is empty, continue until you find a value in the box 
                    continue
                    
                if ( board[r][c] in rows[r]  # if the value in the box is already part of the overall row 
                    or board[r][c] in cols[c] # or if the value in the box is already part of the overall column
                    or board[r][c] in squares[(r // 3, c // 3)]): # or if the value is within the 9x9 square section
                    return False # return False 

                cols[c].add(board[r][c]) # since its not in any of those add the value of that box to that overall column
                rows[r].add(board[r][c]) # and add that value to that overall row 
                squares[(r // 3, c // 3)].add(board[r][c]) # and add that value to that square section 
            

        return True # if no False gets returned by the end of reading the board, it is a valid sudoku board and you can return True
