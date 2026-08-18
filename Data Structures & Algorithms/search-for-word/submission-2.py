class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def backtrack(x, y, i):
            if i == len(word):
                return True
            elif (x >= len(board) or 
            x < 0 or 
            y >= len(board[0]) or
             y < 0 or (x, y) in seen or board[x][y] != word[i]):
                return False
            seen.add((x, y))
            res = (backtrack(x+1, y, i+1) or 
            backtrack(x-1, y, i+1) or 
            backtrack(x, y-1, i+1) or 
            backtrack(x, y+1, i+1))
            seen.remove((x, y))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False

            