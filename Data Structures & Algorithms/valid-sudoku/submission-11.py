class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for y in range(9):
            for x in range(9):
                value = board[y][x]
                if value == '.':
                    continue
                square = squares[y//3][x//3]
                if any([value in rows[y], value in cols[x], value in square]):
                    return False
                    
                rows[y].add(value)
                cols[x].add(value)
                square.add(value)
        return True