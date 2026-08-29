class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(idx):
            if idx == len(empties):
                return True

            row, col = empties[idx]
            b = (row // 3) * 3 + col // 3

            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[b]:
                    # place
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[b].add(num)

                    if backtrack(idx + 1):
                        return True

                    # undo
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack(0)


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = Solution()
solution.solveSudoku(board)

for row in board:
    print(row)