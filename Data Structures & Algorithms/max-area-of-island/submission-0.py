class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(r, c) -> int:
            q = collections.deque()
            q.append([r, c])
            visit.add((r, c))
            area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                r, c = q.popleft()

                for d in directions:
                    new_r = r + d[0]
                    new_c = c + d[1]
                    if ((new_r, new_c) not in visit and
                    new_r in range(len(grid)) and
                    new_c in range(len(grid[0]))):
                        if grid[new_r][new_c] == 1:
                            area += 1
                            q.append([new_r, new_c])
                    visit.add((new_r, new_c))
                    
            
            return area


        visit = set()
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    curr_max = bfs(r, c)
                    maxArea = max(maxArea, curr_max)
        return maxArea

        