class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        self.res = []
        self.backtrack(n, [], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in ans] for ans in self.res]

    def backtrack(self, n, queens, xy_sum, xy_dif):
        row = len(queens)
        if row == n:
            self.res.append(queens)
            return
        for col in range(n):
            if col not in queens and (row+col) not in xy_sum and (row-col) not in xy_dif:
                print(queens)
                self.backtrack(n, queens+[col], xy_sum+[row+col], xy_dif+[row-col])