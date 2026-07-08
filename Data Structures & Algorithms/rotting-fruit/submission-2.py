class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_queue = deque()
        fresh = 0
        minutes = 0

        ROWS, COLS = len(grid), len(grid[0])
        # first count all the fresh, rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        print("rotten queue at the start:", rotten_queue)
        print("fresh at the start:", fresh)

        while rotten_queue and fresh > 0:
            for i in range(len(rotten_queue)):
                row, col = rotten_queue.popleft()
                dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        grid[r][c] = 2
                        rotten_queue.append((r, c))
                        fresh -= 1
                        
                
            minutes += 1

        
        if fresh != 0:
            return -1
        
        else: return minutes
                    


                
