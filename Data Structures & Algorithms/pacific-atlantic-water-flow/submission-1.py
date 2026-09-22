class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        self.heights = heights

        pac, atl = set(), set()

        for c in range(cols):
            self.dfs(0, c, pac, heights[0][c])
            self.dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            self.dfs(r, 0, pac, heights[r][0])
            self.dfs(r, cols - 1, atl, heights[r][cols - 1])

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        
        return ans

    
    def dfs(self, r, c, visit, prevHeight):
        if ((r, c) in visit) or r < 0 or r >= len(self.heights) or c < 0 or c >= len(self.heights[0]) or self.heights[r][c] < prevHeight:
            return
        
        visit.add((r, c))
        self.dfs(r + 1, c, visit, self.heights[r][c])
        self.dfs(r - 1, c, visit, self.heights[r][c])
        self.dfs(r, c + 1, visit, self.heights[r][c])
        self.dfs(r, c - 1, visit, self.heights[r][c])


