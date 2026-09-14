class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3) ]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in rows[i] or val in cols[j] or val in squares[i//3][j//3]:
                        return False
                    else:
                        rows[i].add(val)
                        cols[j].add(val)
                        squares[i//3][j//3].add(val)
        return True