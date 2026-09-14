class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #    0   1   2   3
        # 0  1   2   4   8
        # 1  10  11  12  13
        # 2  14  20  30  40

        def ind(i):
            r = i//COLS
            c = i % COLS

            return r,c
        
        l,r = 0, ROWS*COLS-1

        while l <= r:
            m = (r+l)//2
            mr, mc = ind(m)
            cellv = matrix[mr][mc]

            if cellv == target:
                return True
            elif cellv < target:
                l = m+1
            else:
                r = m-1
        return False

            
