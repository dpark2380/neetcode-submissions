class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()

        # Appending all treasures to queue.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        # Looping through the queue and visiting treasures.
        while queue:
            i, j, dist = queue.popleft()

            if grid[i][j] == 2147483647:
                grid[i][j] = dist
            elif grid[i][j] != 2147483647 and grid[i][j] != 0: 
                continue
            
            if i + 1 < rows and grid[i + 1][j] == 2147483647:
                queue.append((i + 1, j, dist + 1))
            if i - 1 >= 0 and grid[i - 1][j] == 2147483647:
                queue.append((i - 1, j, dist + 1))
            if j + 1 < cols and grid[i][j + 1] == 2147483647:
                queue.append((i, j + 1, dist + 1))
            if j - 1 >= 0 and grid[i][j - 1] == 2147483647:
                queue.append((i, j - 1, dist + 1))




        
   