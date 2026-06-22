class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1


            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1
                    else:
                        continue
            return res
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea

