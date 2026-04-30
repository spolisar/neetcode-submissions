class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        squareSets = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                square = (r // 3) * 3 + (c // 3)
                n = board[r][c]
                if n == '.':
                    continue
                elif n in rowSets[r] or n in colSets[c] or n in squareSets[square]:
                    return False
                rowSets[r].add(n)
                colSets[c].add(n)
                squareSets[square].add(n)
        return True
