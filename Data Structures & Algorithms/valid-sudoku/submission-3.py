class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [set() for _ in range(9)], [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val =='.':
                    continue
                if not ('0'<=val<='9') or val in rows[i] or val in cols[j] or val in squares[i//3][j//3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[i//3][j//3].add(val)
        return True
