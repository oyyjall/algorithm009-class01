class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        self.res = []
        self.backtrack(n, [], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in ans] for ans in self.res]

    def backtrack(self, n, queens, xy_dif, xy_sum):
        # terminator
        row = len(queens)
        if row == n:
            self.res.append(queens)
            return
        for col in range(n):
            if col not in queens and row+col not in xy_dif and row-col not in xy_sum:
                self.backtrack(n, queens+[col], xy_dif+[row+col], xy_sum+[row-col])