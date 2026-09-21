class Solution:
    maxarea = 0
    curarea = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Rows and cols of grid
        r = len(grid)
        if r == 0:
            return 0

        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if (grid[i][j] == 1):
                    self.curarea = 0
                    self.dfs(grid, i, j)
        
        return self.maxarea
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        
        grid[i][j] = 0
        self.curarea += 1
        if self.curarea > self.maxarea:
            self.maxarea = self.curarea

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    

    