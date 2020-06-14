class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.DFS(grid, row, col)
	    count += 1                   
        return count

    def DFS(self, grid, row, col):
        if not (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '2'
        self.DFS(grid, row + 1, col)
        self.DFS(grid, row - 1, col)
        self.DFS(grid, row, col + 1)
        self.DFS(grid, row, col - 1)