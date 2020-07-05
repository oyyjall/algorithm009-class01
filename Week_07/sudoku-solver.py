class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set(range(1, 10)) for _ in range(9)]
        self.cols = [set(range(1, 10)) for _ in range(9)]
        self.block = [set(range(1, 10)) for _ in range(9)]
        self.empty = []
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    cur = int(board[row][col])
                    self.rows[row].remove(cur)
                    self.cols[col].remove(cur)
                    self.block[(row//3)*3+(col//3)].remove(cur)
                else:
                    self.empty.append((row, col))
        self.backtrack(board, 0)

    def backtrack(self, board, iter):
        if iter == len(self.empty):
            return True
        i, j = self.empty[iter]
        b = (i // 3) * 3 + (j // 3)
        for val in self.rows[i] & self.cols[j] & self.block[b]:
            self.rows[i].remove(val)
            self.cols[j].remove(val)
            self.block[b].remove(val)
            board[i][j] = str(val)
            if self.backtrack(board, iter + 1):
                return True
            self.rows[i].add(val)
            self.cols[j].add(val)
            self.block[b].add(val)
        return False