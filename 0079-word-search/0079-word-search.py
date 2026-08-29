class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(row, col, index):
            # Word is completely matched
            if index == len(word):
                return True
            # Out of bounds
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            # Current character doesn't match
            if board[row][col] != word[index]:
                return False

            # Mark the cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Check all 4 directions
            found = (
                dfs(row + 1, col, index + 1) or  # down
                dfs(row - 1, col, index + 1) or  # up
                dfs(row, col + 1, index + 1) or  # right
                dfs(row, col - 1, index + 1)     # left
            )

            # Restore the cell (backtracking)
            board[row][col] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False