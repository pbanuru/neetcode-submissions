class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        def add_item(x,y):
            value = board[y][x]
            cols[x].add(value)
            rows[y].add(value)
            squares[y//3][x//3].add(value)
        
        def is_valid_value(x,y):
            value = board[y][x]
            if any([value in rows[y], value in cols[x], value in squares[y//3][x//3]]):
                return False
            return True

        for y in range(9):
            for x in range(9):
                if board[y][x]=='.':
                    continue
                if not is_valid_value(x,y):
                    return False
                add_item(x,y)
        return True

