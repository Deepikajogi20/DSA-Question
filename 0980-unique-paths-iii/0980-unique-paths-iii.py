from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        startrow, startcol = 0, 0
        empty = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 0:
                    empty += 1
                if grid[r][c] == 1:
                    startrow, startcol = r, c
        return self.dfs(grid, startrow, startcol, empty)

    def dfs(self, grid, r, c, empty):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols or grid[r][c] == -1:
            return 0
        if grid[r][c] == 2:
            return 1 if empty == 0 else 0

        temp = grid[r][c]
        if grid[r][c] == 0:
            empty -= 1
        grid[r][c] = -1

        paths = (self.dfs(grid, r + 1, c, empty) +
                 self.dfs(grid, r - 1, c, empty) +
                 self.dfs(grid, r, c + 1, empty) +
                 self.dfs(grid, r, c - 1, empty))

        grid[r][c] = temp
        return paths