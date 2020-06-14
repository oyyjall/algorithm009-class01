class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []
        directions = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(board), len(board[0])
        row, col = click[0], click[1]
        if board[row][col] == 'M' or board[row][col] == 'X':
            board[row][col] = 'X'
            return board

        num = 0
        for dir in directions:
            newRow = row + dir[0]
            newcol = col + dir[1]
            if newRow >= 0 and newRow < m and newcol >= 0 and newcol < n and board[newRow][newcol] == 'M':
                num += 1
        
        if num > 0:
            board[row][col] = str(num)
            return board

        board[row][col] = 'B'
        for dir in directions:
            newRow = row + dir[0]
            newcol = col + dir[1]
            if newRow >= 0 and newRow < m and newcol >= 0 and newcol < n and board[newRow][newcol] == 'E':
                self.updateBoard(board, (newRow, newcol))
        
        return board