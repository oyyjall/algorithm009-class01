class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        rows, cols, block = set(), set(), set()
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur != '.':
                    if (row, cur) in rows or (cur, col) in cols or ((row//3)*3+(col//3), cur) in block:
                        return False
                    rows.add((row, cur))
                    cols.add((cur, col))
                    block.add(((row//3)*3+(col//3), cur))
        return True