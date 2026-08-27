class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                box=(i//3)*3+(j//3)
                if num in row[i]:
                    return False
                if num in col[j]:
                    return False
                if num in boxes[box]:
                    return False
                row[i].add(num)
                col[j].add(num)
                boxes[box].add(num)
        return True 