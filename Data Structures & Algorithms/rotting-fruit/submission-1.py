class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        if fresh == 0:
            return 0
        
        while queue:
            r, c, t = queue.popleft()

            if grid[r][c] == 1:
                grid[r][c] = 0
                fresh -= 1
                if fresh == 0:
                    return t
            
            if r + 1 < rows and grid[r + 1][c] == 1:
                queue.append((r + 1, c, t + 1))
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                queue.append((r - 1, c, t + 1))
            if c + 1 < cols and grid[r][c + 1] == 1:
                queue.append((r, c + 1, t + 1))
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                queue.append((r, c - 1, t + 1))
        
        return -1