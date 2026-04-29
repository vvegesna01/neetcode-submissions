class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input validation
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    if (new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in visited and grid[new_r][new_c] == "1"):
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
