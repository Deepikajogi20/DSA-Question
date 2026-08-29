class Solution(object):
    def totalNQueens(self, n):
        count = 0
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            nonlocal count
            print(f"-> Entering backtrack(row={row})")
            if row == n:
                count += 1
                print(f"    Solution #{count} found:")
                for r in board:
                    print(f"    {''.join(r)}")
                return

            for col in range(n):

                if col in cols:
                    continue

                if (row - col) in diag1:
                    continue

                if (row + col) in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack: Remove Queen and reset tracking sets
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count


sol = Solution()
n_val = 4
total = sol.totalNQueens(n_val)
print(f"Total solutions for n={n_val}: {total}")