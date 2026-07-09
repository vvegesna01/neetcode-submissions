class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = dr + r, dc + c
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands
        