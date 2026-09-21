class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        r = len(grid)
        if r == 0:
            return 0

        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if (grid[i][j] == '1'):
                    self.dfs(grid, i, j)
                    ans += 1
        
        return ans
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)