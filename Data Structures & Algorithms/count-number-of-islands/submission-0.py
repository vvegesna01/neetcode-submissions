class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # input validation
        if not grid:
            return 0
        
        # get dimensions
        rows, cols = len(grid), len(grid[0])

        # vars
        visit = set()
        islands = 0

        def bfs(r, c):

            q = collections.deque()
            
            visit.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    if (row in range(rows)) and (col in range(cols)) and (grid[row][col] == '1') and ((row, col) not in visit):
                        visit.add((row, col))
                        q.append((row, col))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1' and (r, c) not in visit:

                    bfs(r, c)
                    islands += 1
        
        return islands