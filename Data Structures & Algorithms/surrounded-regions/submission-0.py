class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        self.board = board

        safe = set()

        for r in range(rows):
            self.dfs(r, 0, safe)
            self.dfs(r, cols - 1, safe)
        
        for c in range(cols):
            self.dfs(0, c, safe)
            self.dfs(rows - 1, c, safe)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
    
    def dfs(self, r, c, safe):
        if (r, c) in safe or r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]) or self.board[r][c] == 'X':
            return
        
        safe.add((r, c))

        self.dfs(r + 1, c, safe)
        self.dfs(r - 1, c, safe)
        self.dfs(r, c + 1, safe)
        self.dfs(r, c - 1, safe)

