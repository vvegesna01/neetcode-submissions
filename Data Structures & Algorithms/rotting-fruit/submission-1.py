class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        fresh = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = dr + row, dc + col
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1




