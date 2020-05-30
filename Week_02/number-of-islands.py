class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols, count = len(grid), len(grid[0]), 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == '1':
                    self.DFS(grid, row, col)
                    count += 1
        return count

    def DFS(self, grid, row, col):
        if not self.inArea(grid, row, col):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '2'
        self.DFS(grid, row-1, col)
        self.DFS(grid, row+1, col)
        self.DFS(grid, row, col-1)
        self.DFS(grid, row, col+1)

    def inArea(self, grid, row, col):
        return (row >=0 and row < len(grid)) and (col >= 0 and col < len(grid[0]))
