class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col        

                    if ((r in range(rows)) and c in range(cols)
                        and (r, c) not in visit and grid[r][c] == "1"):
                        visit.add((r, c))
                        q.append((r, c))
                            

        # iterate through the grid
        for r in range(rows):
            for c in range(cols):

                if (r, c) not in visit and grid[r][c] == "1":

                    bfs(r, c)
                    islands += 1
        
        return islands